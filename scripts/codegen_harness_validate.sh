#!/usr/bin/env bash
set -euo pipefail

# Safer globbing & hidden files where needed
shopt -s nullglob dotglob

ROOT="${1:-assets/specs/openapi}"
PORT_BASE="${PORT_BASE:-41000}"
PRISM_FLAGS="${PRISM_FLAGS:---errors=false --multiprocess=false}"
STRICT="${STRICT_CONTRACTS:-false}"   # "true" → specs without paths will fail the job

echo "🔎 Contract test for OpenAPI specs under: ${ROOT}"

mkdir -p .harness_tmp/bundled .harness_logs_contracts .harness_out_contracts

fail=0
idx=0

bundle_spec() {
  local in="$1" out="$2"
  echo "bundling $in..."
  npx -y @redocly/cli@latest bundle "$in" \
    --ext yaml \
    --dereferenced \
    --remove-unused-components \
    -o "$out" >/dev/null
  echo "📦 Created a bundle for $in at $out"
}

has_paths() {
  local spec="$1"
  python3 - "$spec" <<'PY'
import sys, yaml
p = sys.argv[1]
try:
    with open(p, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    print('1' if isinstance(data.get('paths'), dict) and data['paths'] else '0')
except Exception:
    print('0')
PY
}

start_prism() {
  local spec="$1" port="$2" log="$3"
  npx -y @stoplight/prism-cli@5 mock "$spec" \
    -p "$port" -h 127.0.0.1 $PRISM_FLAGS >"$log" 2>&1 &
  echo $!
}

wait_port() {
  local port="$1" tries=30
  for _ in $(seq 1 $tries); do
    if (echo > /dev/tcp/127.0.0.1/"$port") >/dev/null 2>&1; then
      return 0
    fi
    sleep 0.3
  done
  return 1
}

run_schemathesis() {
  local spec="$1" base="$2" outdir="$3"
  # Keep flags compatible with latest Schemathesis; avoid deprecated --seed
  schemathesis run "$spec" \
    --base-url "$base" \
    --checks all \
    --validate-schema \
    --max-examples 10 \
    --hypothesis-deadline=500 \
    --report=md --report-file "$outdir/report.md" >/dev/null
}

# Collect *.yaml and *.yml explicitly (no extglob)
files=( "$ROOT"/C2-*.yaml "$ROOT"/C2-*.yml )

for f in "${files[@]}"; do
  [[ -e "$f" ]] || continue

  base="$(basename "$f")"
  name="${base%.*}"
  port=$((PORT_BASE + idx))
  idx=$((idx + 1))

  echo "──────────────────────────────────────────────────────────────"
  echo "⚙️  Running contract harness for ${base}  (port ${port})"
  echo "──────────────────────────────────────────────────────────────"

  bundled=".harness_tmp/bundled/${base}"
  bundle_spec "$f" "$bundled"

  if [[ "$(has_paths "$bundled")" != "1" ]]; then
    if [[ "$STRICT" == "true" ]]; then
      echo "  ⚠️  No operations found — STRICT=true → failing"
      fail=1
    else
      echo "  ⚠️  No operations found — STRICT=false → skipping"
    fi
    continue
  fi

  log=".harness_logs_contracts/prism_${port}.log"
  pid=$(start_prism "$bundled" "$port" "$log")

  if ! wait_port "$port"; then
    echo "  ❌ Prism failed to open :${port} for ${base}. Last log lines:"
    tail -n 18 "$log" || true
    kill "$pid" >/dev/null 2>&1 || true
    fail=1
    continue
  fi
  echo "  ✅ Prism running on :${port}"

  outdir=".harness_out_contracts/${name}"
  mkdir -p "$outdir"

  if run_schemathesis "$bundled" "http://127.0.0.1:${port}" "$outdir"; then
    echo "  ✅ Schemathesis OK → ${outdir}/report.md"
  else
    echo "  ❌ Schemathesis test failures → ${outdir}/report.md"
    fail=1
  fi

  kill "$pid" >/dev/null 2>&1 || true
done

exit $fail
