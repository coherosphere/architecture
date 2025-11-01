#!/usr/bin/env bash
set -euo pipefail


OPENAPI_ROOT="${1:-assets/specs/openapi}"
PRISM_MODE="${PRISM_MODE:-off}"  # off | soft | strict

OUT_DIR=".harness_out"
TMP_DIR=".harness_tmp"
LOG_DIR=".harness_logs"

SDK_BASE="${OUT_DIR}"
BUNDLE_DIR="${TMP_DIR}/bundled"
PRISM_LOG_DIR="${LOG_DIR}"

PORT_BASE=40100

mkdir -p "${SDK_BASE}" "${BUNDLE_DIR}" "${PRISM_LOG_DIR}"

echo "🔧 Verifying prerequisites…"
# Show versions (best effort)
if command -v node >/dev/null 2>&1; then node -v || true; fi
if command -v npm  >/dev/null 2>&1; then npm -v  || true; fi
if command -v jq   >/dev/null 2>&1; then jq --version || true; fi
if command -v yq   >/dev/null 2>&1; then yq --version || true; fi

if [ ! -d "${OPENAPI_ROOT}" ]; then
  echo "❌ OpenAPI root not found: ${OPENAPI_ROOT}"
  exit 1
fi

echo "🔎 Searching specs under: ${OPENAPI_ROOT}"
mapfile -t FILES < <(find "${OPENAPI_ROOT}" -type f \( -name "*.yaml" -o -name "*.yml" \) | sort)

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "❌ No OpenAPI files found."
  exit 1
fi

echo "📄 OpenAPI files discovered: ${#FILES[@]}"
echo "🔎 DEBUG: Files found:"
for f in "${FILES[@]}"; do
  echo " - ${f}"
done

# ----- helpers ---------------------------------------------------------------

bundle_spec() {
  local in="$1"
  local out="$2"
  npx -y @redocly/cli@latest bundle "${in}" --output "${out}" >/dev/null
  echo "📦 Created a bundle for ${in} at ${out}"
}

has_operations() {
  local bundled="$1"

  local count
  count="$(yq '.paths | length' "${bundled}" 2>/dev/null || echo 0)"
  [[ "${count}" =~ ^[1-9] ]] && return 0 || return 1
}

start_prism() {
  local bundled="$1"
  local port="$2"
  local logf="$3"

  if [ "${PRISM_MODE}" = "off" ]; then
    echo "  (PRISM_MODE=off) Skipping Prism for $(basename "${bundled}")"
    return 0
  fi

  npx -y @stoplight/prism-cli@latest mock \
     --host 127.0.0.1 --port "${port}" \
     --errors=false \
     "${bundled}" > "${logf}" 2>&1 &

  local ok=0
  for _ in {1..30}; do
    if nc -z 127.0.0.1 "${port}" >/dev/null 2>&1; then
      ok=1; break
    fi
    sleep 0.3
  done

  if [ "${ok}" -eq 1 ]; then
    echo "  ✅ Prism running on :${port}"
    return 0
  fi

  echo "  ⚠️  Prism failed to start for $(basename "${bundled}") (port ${port})"
  echo "     See ${logf}"
  echo "----- PRISM LOG (tail) -----"
  tail -n 60 "${logf}" || true
  echo "----------------------------"

  if [ "${PRISM_MODE}" = "strict" ]; then
    return 1
  else
    return 0
  fi
}

generate_sdk() {
  local bundled="$1"
  local outdir="$2"

  npx -y @openapitools/openapi-generator-cli@latest generate \
     -g typescript-fetch \
     -i "${bundled}" \
     -o "${outdir}" >/dev/null

  if [ -f "${outdir}/package.json" ] || [ -d "${outdir}/apis" ] || [ -d "${outdir}/src" ]; then
    return 0
  fi
  return 1
}

# ----- main loop -------------------------------------------------------------

idx=0
PRISM_FAILED=0
CODEGEN_FAILED=0

for spec in "${FILES[@]}"; do
  name="$(basename "${spec}")"
  base="${name%.*}"
  port=$((PORT_BASE + idx))

  echo "▶️  Harness for ${name} (port ${port})"

  bundle_path="${BUNDLE_DIR}/${base}.yaml"
  bundle_spec "${spec}" "${bundle_path}"

  out_sdk="${SDK_BASE}/sdk_${idx}"
  rm -rf "${out_sdk}"
  if generate_sdk "${bundle_path}" "${out_sdk}"; then
    echo "  ✅ Codegen OK → ${out_sdk}"
  else
    echo "  ❌ Codegen failed for ${name}"
    CODEGEN_FAILED=1
  fi

  if has_operations "${bundle_path}"; then
    logf="${PRISM_LOG_DIR}/prism_${idx}.log"
    start_prism "${bundle_path}" "${port}" "${logf}" || PRISM_FAILED=1
  else
    echo "  ℹ️  No operations found — skipping Prism for ${name}"
  fi

  idx=$((idx + 1))
done

echo ""
echo "────────────────────────────────────────────"
echo " Codegen summary:"
echo "   SDK failures:  ${CODEGEN_FAILED}"
echo "   Prism issues:  ${PRISM_FAILED} (mode=${PRISM_MODE})"
echo "────────────────────────────────────────────"


if [ "${CODEGEN_FAILED}" -ne 0 ]; then
  exit 1
fi

if [ "${PRISM_MODE}" = "strict" ] && [ "${PRISM_FAILED}" -ne 0 ]; then
  exit 1
fi

exit 0
