#!/bin/bash
# EXP-006: Lean Companion to Analysis I (teorth/analysis)

set -eo pipefail

PROJECT_DIR="experiments/exp-006-teorth-analysis/analysis"
DIVIDER="----------------------------------------------------------------------------------------------------"

echo "  xLaDe EXP-006: Lean Companion to Analysis I"
echo "  $DIVIDER"
echo "  [info]   Project: $PROJECT_DIR"
echo "  [info]   Running: ./build.sh (lake exe cache get && lake build)"
echo "  $DIVIDER"

cd "$PROJECT_DIR"

build_exit=0

./build.sh 2>&1 | while IFS= read -r line; do
    printf "%s\n" "$line" \
        | fold -s -w 100 \
        | sed 's/^/  /'
done || build_exit=$?

echo "  $DIVIDER"

if [ "$build_exit" -ne 0 ]; then
    echo "  [fail]   build.sh failed."
    exit "$build_exit"
fi

echo "  [pass]   build.sh succeeded."