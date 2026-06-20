#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SMOKE=""
if [[ "${1:-}" == "--smoke-test" ]]; then
  SMOKE="--smoke-test"
fi

echo "==> Building prompts"
python src/build_prompts.py

echo "==> Running evaluation"
python src/run_eval.py $SMOKE

echo "==> Analyzing results"
python src/analyze.py

echo "==> Done. Check results/analysis/summary.json"
