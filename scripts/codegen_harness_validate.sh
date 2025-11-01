#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-assets/specs/openapi}"
BASE_PORT="${BASE_PORT:-41000}"
MAX_EXAMPLES="${MAX_EXAMPLES:-25}"     # shrink/raise for test time
LOG_DIR=".harness_logs_contracts"
OUT_DIR=".harness_contracts"
mkdir -p "$LOG_DIR" "$OUT_DIR"

echo "🔎 Contract test for specs under: $ROOT"
mapfile -t SPECS < <(ls "$ROOT"/C2-*.yaml "$ROOT"/C2-*.yml 2>/dev/null || true)

if [[ ${#SPECS[@]} -eq 0 ]]; then
  echo "❌ No OpenAPI specs found in $ROOT"
  exit 1
fi

pids=()
failures=0

cleanup() {
  echo "🧹 Stopping Prism servers…"
  for pid in "${pids[@]:-}"; do
    if kill -0 "$pid" 2>/dev/null; then kill "$pid" || true; fi
  done
}
trap cleanup EXIT

wait_for_port() {
  local port="$1" tries=40
  while ! (echo >"/dev/tcp/127.0.0.1/$port") >/dev/null 2>&1; do
    sleep 0.25
    tries=$((tries-1))
    [[ $tries -le 0 ]] && return 1
  done
  return 0
}

i=0
for SPEC in "${SPECS[@]}"; do
  fname="$(basename "$SPEC")"
  id="${fname%%.*}"                # e.g., C2-01_Resonance
  port=$((BASE_PORT+i))

  echo ""
  echo "──────────────────────────────────────────────────────────────"
  echo "⚙️  Harness for ${fname}  (port $port)"
  echo "──────────────────────────────────────────────────────────────"

  # 1) Start Prism mock
  LOG="$LOG_DIR/prism_${i}.log"
  echo "  ▶︎ Starting Prism on :$port … (log: $LOG)"
  npx -y @stoplight/prism-cli@5 mock -p "$port" "$SPEC" >"$LOG" 2>&1 & 
  prism_pid=$!
  pids+=("$prism_pid")

  if ! wait_for_port "$port"; then
    echo "  ❌ Prism failed to open port $port (see $LOG)"
    failures=$((failures+1))
    continue
  fi
  echo "  ✅ Prism ready (pid=$prism_pid)"

  # 2) Run Schemathesis against live mock
  JUNIT="$OUT_DIR/${id}_junit.xml"
  RPT="$OUT_DIR/${id}_report.txt"

  echo "  ▶︎ Schemathesis run (max-examples=$MAX_EXAMPLES)…"
  # NOTE: Point schemathesis to the spec file with a base URL to the mock.
  #       This validates that responses from the mock conform to the spec.
  set +e
  schemathesis run "$SPEC" \
    --base-url "http://127.0.0.1:$port" \
    --checks all \
    --stateful=links \
    --hypothesis-seed=1 \
    --hypothesis-max-examples="$MAX_EXAMPLES" \
    --junit-xml "$JUNIT" | tee "$RPT"
  st=$?
  set -e

  if [[ $st -ne 0 ]]; then
    echo "  ❌ Contract violations for $id (exit=$st). See $RPT"
    failures=$((failures+1))
  else
    echo "  ✅ Contract OK for $id (report: $RPT)"
  fi

  # 3) Stop Prism for this spec
  if kill -0 "$prism_pid" 2>/dev/null; then kill "$prism_pid" || true; fi
  i=$((i+1))
done

echo ""
if [[ $failures -gt 0 ]]; then
  echo "❌ Contract test finished with $failures failing spec(s)."
  exit 1
fi
echo "✅ All OpenAPI contracts validated successfully."