#!/bin/bash

# xLaDe kernel protection check
# Fails if lean-core is modified
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "[skip] Not a Git repository. Kernel integrity check skipped."
  exit 0
fi
if git diff --name-only origin/main | grep "^lean-core/" ; then
  echo "  [error]  Kernel modification detected. This violates xLaDe policy."
  exit 1
else
  echo "  [ok]     Kernel untouched."
fi