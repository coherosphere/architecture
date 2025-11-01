#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-assets/specs/openapi}"
BASE_PORT="${BASE_PORT:-41000}"
MAX_EXAMPLES="${MAX_EXAMPLES:-25}"
PRISM_VERSION="${PRISM_VERSION:-5.8.1}"

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

port_free() {
  local port="$1"
  ! lsof -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1
}

wait_for_port() {
  local port="$1" tries=60
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
  id="${fname%%.*}"
  port=$((BASE_PORT+i))

  echo ""
  echo "──────────────────────────────────────────────────────────────"
  echo "⚙️  Harness for ${fname}  (port $port)"
  echo "──────────────────────────────────────────────────────────────"

  if ! port_free "$port"; then
    echo "  ⚠️  Port $port is already in use; skipping."
    failures=$((failures+1))
    continue
  fi

  # Start Prism from the SPEC directory so relative $refs resolve
  LOG="$LOG_DIR/prism_${i}.log"
  SPEC_DIR="$(cd "$(dirname "$SPEC")" && pwd)"
  SPEC_BASENAME="$(basename "$SPEC")"

  echo "  ▶︎ Starting Prism @ $SPEC_DIR on :$port (log: $LOG)"
  (
    cd "$SPEC_DIR"
    npx -y @stoplight/prism-cli@"$PRISM_VERSION" \
      mock "$SPEC_BASENAME" \
      -p "$port" \
      -h 127.0.0.1 \
      --errors
  ) >"$LOG" 2>&1 &

  prism_pid=$!
  pids+=("$prism_pid")

  # Give Prism a moment; if it dies, print logs
  sleep 0.5
  if ! kill -0 "$prism_pid" 2>/dev/null; then
    echo "  ❌ Prism exited immediately for $fname. Last log lines:"
    tail -n 80 "$LOG" || true
    failures=$((failures+1))
    i=$((i+1))
    continue
  fi

  if ! wait_for_port "$port"; then
    echo "  ❌ Prism failed to open :$port for $fname. Last log lines:"
    tail -n 80 "$LOG" || true
    failures=$((failures+1))
    # ensure process is stopped
    kill "$prism_pid" >/dev/null 2>&1 || true
    i=$((i+1))
    continue
  fi
  echo "  ✅ Prism ready (pid=$prism_pid)"

  JUNIT="$OUT_DIR/${id}_junit.xml"
  RPT="$OUT_DIR/${id}_report.txt"

  echo "  ▶︎ Schemathesis run (max-examples=$MAX_EXAMPLES)…"
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

  if kill -0 "$prism_pid" 2>/dev/null; then kill "$prism_pid" || true; fi
  i=$((i+1))
done

echo ""
if [[ $failures -gt 0 ]]; then
  echo "❌ Contract test finished with $failures failing spec(s)."
  exit 1
fi
echo "✅ All OpenAPI contracts validated successfully."
