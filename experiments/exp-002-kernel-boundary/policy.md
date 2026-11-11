# Kernel Boundary Policy — EXP-002

> **Deprecated.** The `lean-core` submodule was removed from xLaDe, so this policy is no longer enforced.
> It is kept for historical reference only.

This experiment enforces the following rule:

> Experiments must not modify `lean-core/`.

Violations are detected via repository scripts and CI checks.

This experiment operationalizes architectural boundaries
described in xLaDe documentation.
