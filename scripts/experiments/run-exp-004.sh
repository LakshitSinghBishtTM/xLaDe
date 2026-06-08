#!/bin/bash

# xLaDe EXP-004: Project Proof 1
# Runs lake build inside the project submodule.
# Pass = lake build exits 0 (all proofs compile).
# Fail = any non-zero exit.

set -e

# Ensure elan-managed binaries (lake, lean) are on PATH.
# Python subprocess does not inherit shell profile modifications.
if [ -f "$HOME/.elan/env" ]; then
  source "$HOME/.elan/env"
fi

PROJECT_DIR="experiments/exp-004-project-proof-1/exp-004-project-proof-1"

echo "  xLaDe EXP-004: Project Proof 1"
echo "  ----------------------------------------------------------------------------------------------------"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "  [error]  Project submodule not found at $PROJECT_DIR"
  echo "           Run: git submodule update --init --recursive"
  exit 1
fi

if [ -z "$(ls -A $PROJECT_DIR)" ]; then
  echo "  [error]  Project submodule is empty."
  echo "           Run: git submodule update --init --recursive"
  exit 1
fi

echo "  [info]   Project: $PROJECT_DIR"
echo "  [info]   Running: lake build"
echo "  ----------------------------------------------------------------------------------------------------"

cd "$PROJECT_DIR"
lake_output=$(lake build 2>&1)
lake_exit=$?

while IFS= read -r line; do
  echo "  $line"
done <<< "$lake_output"

if [ $lake_exit -ne 0 ]; then
  echo "  ----------------------------------------------------------------------------------------------------"
  echo "  [fail]   lake build failed."
  exit $lake_exit
fi

echo "  ----------------------------------------------------------------------------------------------------"
echo "  [pass]   lake build succeeded. All proofs compiled."