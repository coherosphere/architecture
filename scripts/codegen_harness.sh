#!/usr/bin/env bash
set -Eeuo pipefail

# =========================
# Coherosphere Codegen Harness (clean slate)
# - Find all OpenAPI specs under assets/specs/openapi
# - Generate TypeScript SDK types with openapi-typescript
# - Spin up Prism mock per spec, probe a real path/method
# - Produce logs and a summary, fail on first real error
# =========================

ROOT_DEFAULT="assets/specs/openapi"
OUT_DIR=".harness_out"
LOG_DIR=".harness_logs"
PORT_BASE="${PORT_BASE:-40100}"   # you can override in CI if needed
PRISM_VER="@stoplight/prism-cli@5"
OAT_VER="openapi-typescript@latest"

# ---- CLI args (optional) ----
ROOT="${1:-$ROOT_DEFAULT}"

# ---- Ensure tools present ----
need() { command -v "$1" >/dev/null 2>&1 || { echo "❌ Missing dependency: $1"; exit 1; }; }
need curl
need jq
need yq
need node

mkdir -p "$OUT_DIR" "$LOG_DIR"

echo "🔎 Searching specs under: $ROOT"
mapfile -t SPECS < <(find "$ROOT" -type f \( -name "*.yaml" -o -name "*.yml" \) | sort)

if (( ${#SPECS[@]} == 0 )); then
  echo "⚠️  No OpenAPI files found under $ROOT"
  exit 0
fi

# Pick first usable operation (prefer GET, else POST, PUT, PATCH, DELETE)
pick_first_operation() {
  local spec="$1"
  # returns "METHOD PATH" or empty string
  # Try GET first
  local res
  res="$(yq -r '
    .paths
    | to_entries
    | [ .[] | select(.value.get) | {m:"GET", p:.key} ][0]
  ' "$spec" 2>/dev/null || true)"

  if [[ -n "$res" && "$res" != "null" ]]; then
    local p; p="$(echo "$res" | yq -r '.p' 2>/dev/null || true)"
    if [[ -n "$p" && "$p" != "null" ]]; then
      echo "GET $p"
      return 0
    fi
  fi

  # Else first operation of any method (stable order)
  res="$(yq -r '
    .paths
    | to_entries
    | [ .[] |
        ( .value | to_entries | map(.key | ascii_upcase) | sort )[0] as $m
        | {m:$m, p:.key}
      ][0]
  ' "$spec" 2>/dev/null || true)"

  if [[ -n "$res" && "$res" != "null" ]]; then
    local m p
    m="$(echo "$res" | yq -r '.m' 2>/dev/null || true)"
    p="$(echo "$res" | yq -r '.p' 2>/dev/null || true)"
    if [[ -n "$m" && -n "$p" && "$m" != "null" && "$p" != "null" ]]; then
      echo "$m $p"
      return 0
    fi
  fi

  # Nothing found
  echo ""
  return 1
}

wait_until_http_ok() {
  # Args: URL, max_tries, sleep_seconds
  local url="$1"; local tries="${2:-60}"; local nap="${3:-0.3}"
  local code
  for _ in $(seq 1 "$tries"); do
    code="$(curl -sS -o /dev/null -w "%{http_code}" "$url" || true)"
    if [[ "$code" =~ ^(200|201|202|204|400|401|403|404)$ ]]; then
      return 0
    fi
    sleep "$nap"
  done
  return 1
}

# For non-GET we send a minimal JSON body
probe_with_method() {
  # Args: METHOD URL OUTFILE
  local method="$1" url="$2" outfile="$3" code
  case "$method" in
    GET|DELETE)
      code="$(curl -sS -o "$outfile" -w "%{http_code}" -X "$method" "$url" || true)"
      ;;
    POST|PUT|PATCH|OPTIONS)
      code="$(curl -sS -o "$outfile" -w "%{http_code}" -X "$method" \
              -H 'content-type: application/json' \
              --data '{}' "$url" || true)"
      ;;
    *)
      code="$(curl -sS -o "$outfile" -w "%{http_code}" "$url" || true)"
      ;;
  esac
  echo "$code"
}

status_overall=0
idx=0

for spec in "${SPECS[@]}"; do
  ((idx++))
  rel="${spec#*/}"                         # relative for logs
  port=$(( PORT_BASE + idx ))
  sdk_dir="${OUT_DIR}/sdk_${idx}"
  prism_log="${LOG_DIR}/prism_${idx}.log"
  resp_out="${LOG_DIR}/resp_${idx}.json"

  echo ""
  echo "==============================="
  echo "Harness for: $rel"
  echo "Port:        $port"
  echo "SDK out:     $sdk_dir"
  echo "Log:         $prism_log"
  echo "==============================="

  rm -rf "$sdk_dir"
  mkdir -p "$sdk_dir"

  # ---- Codegen (Types) ----
  echo "🛠  Generating TypeScript types with openapi-typescript…"
  if ! npx -y "$OAT_VER" "$spec" -o "${sdk_dir}/types.ts" >/dev/null 2>&1; then
    echo "::error ::openapi-typescript failed for $rel"
    status_overall=1
    continue
  fi
  echo "✅ Codegen OK → ${sdk_dir}/types.ts"

  # ---- Start Prism (mock) ----
  echo "🚀 Starting Prism mock on 127.0.0.1:${port}…"
  set +e
  npx -y "$PRISM_VER" mock -h 127.0.0.1 -p "$port" "$spec" >"$prism_log" 2>&1 &
  pid=$!
  set -e

  # ---- Determine probe endpoint ----
  op="$(pick_first_operation "$spec" || true)"
  method="GET"
  path="/"
  if [[ -n "$op" ]]; then
    method="$(awk '{print $1}' <<<"$op")"
    path="$(awk '{print $2}' <<<"$op")"
  fi
  url="http://127.0.0.1:${port}${path}"
  echo "🔎 Selected operation: ${method} ${path}"

  # ---- Wait until Prism responds on that URL (allow common 2xx/4xx) ----
  echo "⏳ Waiting for mock readiness on: $url"
  if ! wait_until_http_ok "$url" 80 0.25; then
    echo "::group::Prism log (first 200 lines) – $rel"
    sed -n '1,200p' "$prism_log" || true
    echo "::endgroup::"
    echo "::error ::Prism didn’t respond on $url (spec: $rel)"
    kill "$pid" >/dev/null 2>&1 || true
    status_overall=1
    continue
  fi

  # ---- Probe request ----
  echo "📡 Probing ${method} ${url}"
  code="$(probe_with_method "$method" "$url" "$resp_out")"
  if [[ "$code" =~ ^(200|201|202|204|400|401|403|404)$ ]]; then
    echo "✅ Mock response $code for $rel (${method} ${path})"
  else
    echo "::group::Prism log (first 200 lines) – $rel"
    sed -n '1,200p' "$prism_log" || true
    echo "::endgroup::"
    echo "::group::Response body – $rel"
    sed -n '1,120p' "$resp_out" 2>/dev/null || true
    echo "::endgroup::"
    echo "::error ::Unexpected status $code for $rel (${method} ${path})"
    status_overall=1
  fi

  # ---- Cleanup mock ----
  kill "$pid" >/dev/null 2>&1 || true
done

echo ""
if [[ "$status_overall" -eq 0 ]]; then
  echo "🎉 Harness completed successfully for ${#SPECS[@]} spec(s)."
else
  echo "❌ Harness finished with errors. See ${LOG_DIR}/* and summary above."
fi

exit "$status_overall"