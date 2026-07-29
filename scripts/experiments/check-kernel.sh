#!/usr/bin/env bash
set -euo pipefail

# Check both the lean-core gitlink and any local submodule edits.
KERNEL_PATH="lean-core"
BASE_REF="${KERNEL_BASE_REF:-origin/main}"

fail() {
  echo "  [error]  $1"
  exit 1
}

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "Kernel check requires a Git work tree."
git rev-parse --verify --quiet "${BASE_REF}^{commit}" >/dev/null || fail "Cannot verify baseline: ${BASE_REF}"

MERGE_BASE="$(git merge-base "$BASE_REF" HEAD)" || fail "Cannot find a common ancestor with: ${BASE_REF}"

# A submodule is recorded as one gitlink entry named exactly "lean-core".
if ! git diff --quiet --ignore-submodules=none "$MERGE_BASE" HEAD -- "$KERNEL_PATH"; then
  fail "lean-core submodule revision changed."
fi

# An initialized submodule has its own .git file (or directory).
[ -e "$KERNEL_PATH/.git" ] || fail "lean-core is not initialized."

# This also detects dirty files inside a populated submodule.
if ! git diff --quiet --ignore-submodules=none -- "$KERNEL_PATH"; then
  fail "lean-core has uncommitted changes."
fi

echo "  [ok]     Kernel untouched."
