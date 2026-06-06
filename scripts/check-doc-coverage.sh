#!/bin/bash

# xLaDe EXP-003: Documentation Coverage Check
# Verifies required README.md files exist across the repo structure.

set -e

ERRORS=0

check_readme() {
  local dir=$1
  local label=$2

  if [ ! -f "$dir/README.md" ]; then
    echo "  [error]  Missing README.md in $label: $dir"
    ERRORS=$((ERRORS + 1))
  else
    echo "  [ok]     $label: $dir"
  fi
}

echo "  xLaDe Doc Coverage Check"
echo "  -------------------------"

# Check experiments/
if [ -d "experiments" ]; then
  for dir in experiments/*/; do
    [ -d "$dir" ] || continue
    name=$(basename "$dir")
    [[ "$name" == *.* ]] && continue
    check_readme "$dir" "experiment"
  done
else
  echo "  [error]  experiments/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

# Check modes/
if [ -d "modes" ]; then
  for dir in modes/*/; do
    [ -d "$dir" ] || continue
    check_readme "$dir" "mode"
  done
else
  echo "  [error]  modes/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

# Check policies/
if [ -d "policies" ]; then
  count=$(find policies/ -maxdepth 1 -name "*.md" | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "  [error]  No .md files found in policies/"
    ERRORS=$((ERRORS + 1))
  else
    echo "  [ok]     policies/ has $count documentation file(s)"
  fi
else
  echo "  [error]  policies/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

echo "  -------------------------"

if [ "$ERRORS" -eq 0 ]; then
  echo "  [pass]   All documentation checks passed."
  exit 0
else
  echo "  [fail]   $ERRORS documentation issue(s) found."
  exit 1
fi