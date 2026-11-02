#!/usr/bin/env bash
# P3-05: Shell runner for isolated AI agent runs (Linux / macOS / WSL / Git Bash)
# Usage:
#   ./scripts/p3_05_run_agent.sh claude A-01
#   ./scripts/p3_05_run_agent.sh codex B-01
#   ./scripts/p3_05_run_agent.sh gemini C-01

set -euo pipefail

FAMILY="${1:-}"
RUN_ID="${2:-}"

if [ -z "$FAMILY" ] || [ -z "$RUN_ID" ]; then
    echo "Usage: $0 <claude|codex|gemini> <run_id>"
    echo "Example: $0 claude A-01"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
BUNDLE_DIR="${ROOT_DIR}/data/agentic_bundle"
RUNS_DIR="${ROOT_DIR}/results/agentic/runs"

if [ ! -d "$BUNDLE_DIR" ]; then
    echo "ERROR: Bundle directory $BUNDLE_DIR not found. Run python scripts/p3_05_build_bundle.py first."
    exit 1
fi

TMP_DIR="/tmp/agent_run_${FAMILY}_${RUN_ID}"
echo "=== Initializing isolated sandbox in: $TMP_DIR ==="
rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"

# Copy frozen bundle and docs
cp -r "${BUNDLE_DIR}/"* "$TMP_DIR/"

# Prepare frozen PROMPT.txt
cat << 'EOF' > "${TMP_DIR}/PROMPT.txt"
You are an empirical economist. The folder `data/` contains hourly USDT/BRL prices from Binance, the Brazilian central bank's official dollar rate (PTAX) and hourly USDC/USDT prices, with the providers' documentation in `docs/`. Question: did the price of USDT in reais, relative to the official dollar, change after 23 June 2026, and by how much? Estimate the change in basis points with a standard error. Make and justify your own analysis choices. Use only the files provided. Write your code to `analysis.py`, your answer to `answer.json` (schema below) and a short explanation (<= 300 words) to `report.md`.

Required JSON schema for answer.json:
{
  "run_id": "__RUN_ID__",
  "model": "<model name and exact version string>",
  "direction": "up | down | no change",
  "estimate_bps": 0.0,
  "std_error_bps": 0.0,
  "premium_definition": "<formula in words>",
  "time_matching": "<how USDT/BRL and PTAX were aligned in time>",
  "usdt_usd_adjustment": false,
  "window_pre_days": 0,
  "window_post_days": 0,
  "estimator": "<difference in means, regression, ...>",
  "controls": [],
  "data_issues_found": [],
  "notes": "<concise summary of findings>"
}
EOF

# Inject the exact run_id
sed -i.bak "s/__RUN_ID__/${RUN_ID}/g" "${TMP_DIR}/PROMPT.txt" && rm -f "${TMP_DIR}/PROMPT.txt.bak"

echo "Sandbox initialized. Executing ${FAMILY} agent CLI..."
PROMPT_CONTENT=$(cat "${TMP_DIR}/PROMPT.txt")
START_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cd "$TMP_DIR"
set +e

if [ "$FAMILY" = "claude" ]; then
    # Claude Code: non-interactive print mode
    claude --dangerously-skip-permissions -p "$PROMPT_CONTENT" > run.log 2>&1
    EXIT_CODE=$?
elif [ "$FAMILY" = "codex" ]; then
    # Codex CLI
    codex exec --prompt "$PROMPT_CONTENT" > run.log 2>&1
    EXIT_CODE=$?
elif [ "$FAMILY" = "gemini" ]; then
    # Gemini CLI
    gemini prompt "$PROMPT_CONTENT" > run.log 2>&1
    EXIT_CODE=$?
else
    echo "Unknown family: $FAMILY. Must be claude, codex, or gemini."
    exit 1
fi

set -e
cd "$ROOT_DIR"
END_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "Agent CLI execution finished (exit code: $EXIT_CODE). Validating and archiving..."

# Run python validator to check schema and archive
python3 scripts/p3_05_harness.py --run-id "$RUN_ID" --validate-dir "$TMP_DIR"
echo "=== Run $RUN_ID completed and archived to results/agentic/runs/${RUN_ID} ==="
