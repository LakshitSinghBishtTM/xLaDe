#!/bin/bash
# EXP-007: AND/OR Proof

set -e

if [ -f "$HOME/.elan/env" ]; then
  source "$HOME/.elan/env"
fi

PROJECT_DIR="experiments/exp-007-and-or/proof"
DIVIDER="----------------------------------------------------------------------------------------------------"
FILES=("true_statement.lean" "false_statement.lean")

echo "  xLaDe EXP-7: And OR Proof"
echo "  $DIVIDER"
echo "  [info]   Project: $PROJECT_DIR"

cd "$PROJECT_DIR"

if cache_output=$(lake exe cache get 2>&1); then
    cache_exit=0
else
    cache_exit=$?
fi

while IFS= read -r line; do
    echo "  $line"
done <<< "$cache_output"

if [ "$cache_exit" -ne 0 ]; then
    echo "  $DIVIDER"
    echo "  [fail]   lake exe cache get failed."
    exit "$cache_exit"
fi

echo "  $DIVIDER"

overall_exit=0

for f in "${FILES[@]}"; do
    echo "  -- $f --"

    if file_output=$(lake env lean "$f" 2>&1); then
        file_exit=0
    else
        file_exit=$?
    fi

    while IFS= read -r line; do
        echo "    $line"
    done <<< "$file_output"

    if [ "$file_exit" -ne 0 ]; then
        overall_exit=1
        echo "  [fail]  $f"
    else
        echo "  [pass]  $f"
    fi
done

echo "  $DIVIDER"

if [ "$overall_exit" -ne 0 ]; then
    echo "  [fail]   one or more files failed to type-check."
    exit "$overall_exit"
fi

echo "  [pass]   both files type-checked."
