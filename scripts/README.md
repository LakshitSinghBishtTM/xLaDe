# xLaDe Scripts

This directory contains **auxiliary scripts** used to orchestrate Lean-related
workflows across the xLaDe repository. Scripts operate at the **repository and
ecosystem level**, not at the language or kernel level. They exist to support
policy enforcement, experiment coordination, and structural validation.

---

## What Scripts Are (and Are Not)

### Scripts **ARE**
- Repository-level helpers for:
  - enforcing policies
  - running or coordinating experiments
  - validating structural constraints
- Usable both:
  - locally by contributors
  - automatically in CI environments
- Explicit, inspectable, and replaceable

### Scripts **ARE NOT**
- Modifications to Lean core or kernel
- Changes to Lean semantics or proof behavior
- Required for normal Lean usage outside xLaDe
- Hidden or implicit enforcement mechanisms

Scripts must never alter Lean source code or trusted semantics.

---

## Important: elan PATH

Scripts that invoke `lake` or `lean` must source elan's environment at the
top of the script. Python's subprocess does not inherit shell profile
modifications (`.zshrc`, `.bash_profile`, etc.), so elan-managed binaries
will not be on PATH unless explicitly sourced.

Add this block after `set -e` in every experiment script that uses lake or lean:

```bash
if [ -f "$HOME/.elan/env" ]; then
  source "$HOME/.elan/env"
fi
```

This applies to all platforms — macOS, Linux, and Android (Termux). Without
it, scripts will fail with `lake: command not found` even when lake is
correctly installed.

---

## Current Scripts

| Script                   | Used by                    | Purpose                              |
|--------------------------|----------------------------|--------------------------------------|
| `check-kernel.sh`        | `exp-002-kernel-boundary`  | Check the `lean-core` revision and local edits |
| `check-doc-coverage.sh`  | `exp-003-doc-coverage`     | Verify README.md presence in dirs    |
| `run-exp-004.sh`         | `exp-004-project-proof-1`  | Run `lake build` on external project |
| `run-exp-005.sh`         | `exp-005-lean4-courses`    | Run `lake build` on external project |
| `run-exp-006.sh`         | `exp-006-teorth-analysis`  | Run the external `build.sh`          |
| `run-exp-007.sh`         | `exp-007-and-or`           | Check two AND/OR proof files        |

---

## Design Constraints

All scripts must adhere to the following constraints:

- **Non-invasive** — scripts must not modify Lean kernel sources or semantics
- **Transparent** — script behavior should be clear from inspection
- **Reversible** — removing a script or CI hook must disable enforcement without side effects

These constraints reflect xLaDe's research-first and safety-oriented design.

---

## Summary

xLaDe scripts provide a **lightweight enforcement and orchestration layer**
around Lean usage. They support disciplined ecosystem experimentation, protect
architectural boundaries, and integrate cleanly with CI workflows, while
keeping Lean's trusted core untouched.
