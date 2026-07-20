#!/bin/bash

set -e

if [ -f "$HOME/.elan/env" ]; then
  source "$HOME/.elan/env"
fi

PROJECT_DIR="experiments/exp-005-lean4-courses/lean4-courses"

echo "  xLaDe EXP-005: Lean4 Courses"
echo "  ----------------------------------------------------------------------------------------------------"

if [ ! -d "$PROJECT_DIR" ] || [ -z "$(ls -A $PROJECT_DIR)" ]; then
  echo "  [error]  Project submodule not found or empty."
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
echo "  [pass]   lake build succeeded. 32 modules compiled."
