#!/usr/bin/env bash
set -euo pipefail

OPENAPI_ROOT="${1:-assets/specs/openapi}"
PRISM_MODE="${PRISM_MODE:-off}"          # off | mock | test (you already set off)
GENERATOR="${GENERATOR:-typescript-fetch}"

echo "🔧 Verifying prerequisites…"
node -v
npm -v
jq --version || true
yq --version || true

echo "🔎 Searching specs under: ${OPENAPI_ROOT}"
mapfile -t FILES < <(ls -1 "${OPENAPI_ROOT}"/*.y*ml | sort)
echo "📄 OpenAPI files discovered: ${#FILES[@]}"

mkdir -p .harness_tmp/bundled .harness_out .harness_logs

sdk_failures=0
prism_failures=0
idx=0
base_port=40100

has_ops() {
  # Return 0 (true) if the bundled YAML contains at least one HTTP operation
  # Grep is robust enough here and way quicker than fancy yq filters.
  local bundled="$1"
  grep -Eq '^\s*(get|post|put|delete|patch|options|head|trace):\s*$' "$bundled"
}

for f in "${FILES[@]}"; do
  svc="$(basename "$f")"
  port=$((base_port + idx))
  echo "▶️  Harness for ${svc} (port ${port})"

  # 1) Bundle (fully-resolve $ref) with Redocly
  echo "bundling ${f}..."
  npx -y @redocly/cli@latest bundle "${f}" -o ".harness_tmp/bundled/${svc}" >/dev/null
  echo "📦 Created a bundle for ${f} at .harness_tmp/bundled/${svc}"

  bundled=".harness_tmp/bundled/${svc}"

  if ! has_ops "${bundled}"; then
    echo "  ℹ️  No operations found — skipping SDK/Prism for ${svc}"
    idx=$((idx + 1))
    continue
  fi

  # 2) SDK codegen (only if operations exist)
  outdir=".harness_out/sdk_${idx}"
  rm -rf "${outdir}"
  if npx -y @openapitools/openapi-generator-cli@latest generate \
      -g "${GENERATOR}" -i "${bundled}" -o "${outdir}" >/dev/null 2>&1; then
    echo "  ✅ Codegen OK → ${outdir}"
  else
    echo "  ❌ Codegen failed for ${svc}"
    sdk_failures=$((sdk_failures + 1))
    idx=$((idx + 1))
    # if codegen fails, Prism would be pointless; skip to next file
    continue
  fi

  # 3) Optional Prism (mock/test)
  if [[ "${PRISM_MODE}" != "off" ]]; then
    log=".harness_logs/prism_${idx}.log"
    if npx -y @stoplight/prism-cli@latest mock "${bundled}" \
        --host 127.0.0.1 --port "${port}" --errors=false >"${log}" 2>&1 & then
      # give Prism a blink to bind
      sleep 0.6
      if grep -qi "listening" "${log}" || nc -z 127.0.0.1 "${port}"; then
        echo "  ✅ Prism running on :${port}"
      else
        echo "  ⚠️  Prism started but did not bind :${port} → ${log}"
        prism_failures=$((prism_failures + 1))
      fi
    else
      echo "  ❌ Prism failed to start for ${svc} (port ${port}). See ${log}"
      prism_failures=$((prism_failures + 1))
    fi
  else
    echo "  (PRISM_MODE=off) Skipping Prism for ${svc}"
  fi

  idx=$((idx + 1))
done

echo "────────────────────────────────────────────"
echo " Codegen summary:"
echo "   SDK failures:  ${sdk_failures}"
echo "   Prism issues:  ${prism_failures} (mode=${PRISM_MODE})"
echo "────────────────────────────────────────────"

# Exit non-zero only if there are REAL failures (on specs with operations)
if (( sdk_failures > 0 || prism_failures > 0 )); then
  exit 1
fi
exit 0
