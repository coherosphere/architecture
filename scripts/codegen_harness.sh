#!/usr/bin/env bash
set -euo pipefail

ROOT="assets/specs/openapi"
LOG_DIR=".harness_logs"
OUT_DIR=".harness_out"

mkdir -p "$LOG_DIR" "$OUT_DIR"

echo "::group::Discover OpenAPI specs"
mapfile -t SPECS < <(find "$ROOT" -type f \( -name "*.yaml" -o -name "*.yml" \) | sort)
printf "Found %d specs\n" "${#SPECS[@]}"
echo "::endgroup::"

fail() { echo "::error ::$*"; exit 1; }

check_x_c2_id() {
  local spec="$1"
  local id
  id="$(yq -r '.info."x-c2-id"' "$spec" 2>/dev/null || true)"
  [[ -n "$id" && "$id" != "null" ]] || fail "Missing info.x-c2-id in $spec"
  local fname; fname="$(basename "$spec")"
  if [[ "$fname" != *"${id}"* ]]; then
    echo "::warning ::Filename ($fname) does not include x-c2-id ($id)."
  fi
}

pick_first_path() {
  local spec="$1"
  local first_get first_any
  first_get="$(yq -r '.paths | to_entries | map(select(.value.get)) | .[0].key' "$spec" 2>/dev/null || true)"
  first_any="$(yq -r '.paths | keys | .[0]' "$spec" 2>/dev/null || true)"
  if [[ -n "$first_get" && "$first_get" != "null" ]]; then
    echo "$first_get"
  else
    echo "$first_any"
  fi
}

start_prism() {
  local spec="$1" port="$2" log="$3"
  npx -y @stoplight/prism-cli@5 mock "$spec" -h 127.0.0.1 -p "$port" >"$log" 2>&1 &
  echo $!
}

wait_for_port() {
  local port="$1" tries=50
  for _ in $(seq 1 $tries); do
    if curl -sSf "http://127.0.0.1:${port}/__docs" >/dev/null 2>&1; then
      return 0
    fi
    sleep 0.2
  done
  return 1
}

gen_sdk() {
  local spec="$1" outdir="$2"
  rm -rf "$outdir"
  mkdir -p "$outdir"
  openapi-generator-cli generate \
    -i "$spec" \
    -g typescript-axios \
    -o "$outdir" \
    --skip-validate-spec > /dev/null 2>&1 || return 1
}

status_overall=0
port_base=40100

for idx in "${!SPECS[@]}"; do
  spec="${SPECS[$idx]}"
  rel="${spec#$ROOT/}"
  echo "::group::Harness for $rel"

  check_x_c2_id "$spec"

  sdk_dir="$OUT_DIR/sdk_${idx}"
  if gen_sdk "$spec" "$sdk_dir"; then
    echo "✅ Codegen OK → $sdk_dir"
  else
    echo "::error ::Codegen failed for $rel"
    status_overall=1
  fi

  port=$((port_base + idx))
  prism_log="$LOG_DIR/prism_${idx}.log"
  pid="$(start_prism "$spec" "$port" "$prism_log")"
  echo "Prism PID=$pid on port $port (logs: $prism_log)"

  if ! wait_for_port "$port"; then
    echo "::error ::Prism failed to start for $rel (port $port). See $prism_log"
    kill "$pid" >/dev/null 2>&1 || true
    status_overall=1
    echo "::endgroup::"
    continue
  fi

  path="$(pick_first_path "$spec")"
  if [[ -z "$path" || "$path" == "null" ]]; then
    echo "::warning ::No paths found in $rel — skipping HTTP probe."
    kill "$pid" >/dev/null 2>&1 || true
    echo "::endgroup::"
    continue
  fi

  url="http://127.0.0.1:${port}${path}"
  echo "Probing: GET $url"
  if curl -sS -o "$LOG_DIR/resp_${idx}.json" -w "%{http_code}" "$url" | grep -qE "^(200|201)$"; then
    echo "✅ Mock response OK for $rel ($path)"
  else
    echo "::error ::Mock probe failed for $rel ($path). See $prism_log"
    status_overall=1
  fi

  kill "$pid" >/dev/null 2>&1 || true
  echo "::endgroup::"
done

echo "Harness overall status: $status_overall"
exit "$status_overall"