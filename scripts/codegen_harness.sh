#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="${1:-assets/specs/openapi}"
OUT_DIR=".harness_out"
LOG_DIR=".harness_logs"
BASE_PORT=40100
DEBUG="${HARNESS_DEBUG:-1}"

log()  { echo -e "$@"; }
dbg()  { [[ "$DEBUG" == "1" ]] && echo "🔎 DEBUG: $*" || true; }

# --- Prepare directories ---
mkdir -p "$OUT_DIR" "$LOG_DIR"

# --- Dependency check ---
log "🔧 Verifying prerequisites…"
missing=0
for bin in node npm jq curl yq; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    log "❌ Missing dependency: $bin"
    missing=1
  else
    dbg "✅ Found $bin: $(command -v "$bin")"
  fi
done
if [[ $missing -eq 1 ]]; then
  log "❌ Aborting due to missing dependencies."
  exit 1
fi

# --- Locate OpenAPI specs ---
log "🔎 Searching specs under: $ROOT"
if [[ ! -d "$ROOT" ]]; then
  log "❌ Directory not found: $ROOT"
  exit 1
fi

mapfile -t SPECS < <(find "$ROOT" -type f \( -name "*.yaml" -o -name "*.yml" \) | sort)
COUNT=${#SPECS[@]}
log "📄 OpenAPI files discovered: $COUNT"
if [[ $COUNT -eq 0 ]]; then
  log "⚠️  No OpenAPI files found. Exiting gracefully."
  exit 0
fi

dbg "Files found:"
for s in "${SPECS[@]}"; do echo " - $s"; done

# --- Stage 2: Mock + Probe ---
PRISM_BIN="npx -y @stoplight/prism-cli@latest mock"
i=0
overall=0

for spec in "${SPECS[@]}"; do
  port=$((BASE_PORT + i))
  name="$(basename "$spec")"
  log "\n▶️  Harness for $name (port $port)"
  LOGFILE="$LOG_DIR/prism_${i}.log"

  # Codegen placeholder (optional)
  mkdir -p "$OUT_DIR/sdk_${i}"
  echo "Codegen stub for $name" > "$OUT_DIR/sdk_${i}/readme.txt"
  log "  ✅ Codegen OK → $OUT_DIR/sdk_${i}"

  # Start Prism in background
  nohup $PRISM_BIN "$spec" -h 127.0.0.1 -p "$port" >"$LOGFILE" 2>&1 &
  prism_pid=$!

  # Wait up to 12s for Prism to start
  ready=0
  for t in {1..12}; do
    if curl -sf "http://127.0.0.1:$port" >/dev/null 2>&1; then
      log "  ✅ Prism ready (PID=$prism_pid, port=$port)"
      ready=1
      break
    fi
    sleep 1
  done

  if [[ $ready -eq 0 ]]; then
    log "  ⚠️  Prism failed to start for $name (port $port)"
    log "     See $LOGFILE"
    kill "$prism_pid" >/dev/null 2>&1 || true
    i=$((i+1))
    continue
  fi

  # Probe root path
  if curl -sf "http://127.0.0.1:$port" >/dev/null 2>&1; then
    log "  🟢 Probe OK for $name"
  else
    log "  🟡 Probe warning for $name"
    overall=1
  fi

  kill "$prism_pid" >/dev/null 2>&1 || true
  i=$((i+1))
done

log "\n🏁 Harness completed. Logs → $LOG_DIR"
exit 0