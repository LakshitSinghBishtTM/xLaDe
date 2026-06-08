#!/bin/bash

# xLaDe kernel protection check
# Fails if lean-core is modified

if git diff --name-only origin/main | grep "^lean-core/" ; then
  echo "  [error]  Kernel modification detected. This violates xLaDe policy."
  exit 1
else
  echo "  [ok]     Kernel untouched."
fi