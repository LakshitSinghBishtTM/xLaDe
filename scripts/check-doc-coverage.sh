#!/bin/bash

# xLaDe EXP-003: Documentation Coverage Check
# Verifies required README.md files exist across the repo structure.

set -e

ERRORS=0

check_readme() {
  local dir=$1
  local label=$2

  if [ ! -f "$dir/README.md" ]; then
    echo "❌ Missing README.md in $label: $dir"
    ERRORS=$((ERRORS + 1))
  else
    echo "✅ $label: $dir"
  fi
}

echo "xLaDe Doc Coverage Check"
echo "========================="

# Check experiments/
if [ -d "experiments" ]; then
  for dir in experiments/*/; do
    [ -d "$dir" ] || continue
    name=$(basename "$dir")
    # Skip non-experiment dirs (files, templates etc)
    [[ "$name" == *.* ]] && continue
    check_readme "$dir" "experiment"
  done
else
  echo "❌ experiments/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

# Check modes/
if [ -d "modes" ]; then
  for dir in modes/*/; do
    [ -d "$dir" ] || continue
    check_readme "$dir" "mode"
  done
else
  echo "❌ modes/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

# Check policies/
if [ -d "policies" ]; then
  count=$(find policies/ -maxdepth 1 -name "*.md" | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "❌ No .md files found in policies/"
    ERRORS=$((ERRORS + 1))
  else
    echo "✅ policies/ has $count documentation file(s)"
  fi
else
  echo "❌ policies/ directory not found"
  ERRORS=$((ERRORS + 1))
fi

echo "========================="

if [ "$ERRORS" -eq 0 ]; then
  echo "✅ All documentation checks passed."
  exit 0
else
  echo "❌ $ERRORS documentation issue(s) found."
  exit 1
fi