#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-assets/specs/openapi}"
PORT_BASE="${PORT_BASE:-41000}"
PRISM_FLAGS="${PRISM_FLAGS:---errors=false --multiprocess=false}"
STRICT="${STRICT_CONTRACTS:-false}"   # true = fehlende paths => Fehler

echo "🔎 Contract test for specs under: ${ROOT}"

mkdir -p .harness_tmp/bundled .harness_logs_contracts .harness_out_contracts

fail=0
idx=0

bundle_spec() {
  local in="$1" out="$2"
  # Redocly CLI (neu)
  npx -y @redocly/cli@latest bundle "$in" \
    --ext yaml \
    --dereferenced \
    --remove-unused-components \
    -o "$out" >/dev/null
}

has_paths() {
  python3 - "$1" <<'PY'
import sys, yaml
p = sys.argv[1]
try:
    with open(p, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    print('1' if (data or {}).get('paths') else '0')
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
  schemathesis run "$spec" \
    --base-url "$base" \
    --checks all \
    --validate-schema \
    --max-examples 10 \
    --hypothesis-deadline=500 \
    --seed 42 \
    --report=md --report-file "$outdir/report.md" >/dev/null
}

shopt -s nullglob
for f in "$ROOT"/C2-*.y?(a)ml; do
  base="$(basename "$f")"
  name="${base%.*}"
  port=$((PORT_BASE + idx))
  idx=$((idx + 1))

  echo "──────────────────────────────────────────────────────────────"
  echo "⚙️  Harness for ${base}  (port ${port})"
  echo "──────────────────────────────────────────────────────────────"

  bundled=".harness_tmp/bundled/${base}"
  bundle_spec "$f" "$bundled"

  if [[ "$(has_paths "$bundled")" != "1" ]]; then
    echo "  ⚠️  No operations found — ${STRICT:+failing}${STRICT:-skipping}"
    if [[ "$STRICT" == "true" ]]; then fail=1; fi
    continue
  fi

  log=".harness_logs_contracts/prism_${idx}.log"
  pid=$(start_prism "$bundled" "$port" "$log")

  if ! wait_port "$port"; then
    echo "  ❌ Prism failed to open :${port} for ${base}. Last log lines:"
    tail -n 12 "$log" || true
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
