import Lake
open Lake DSL

/--
xLaDe: Experimental Lean 4 Ecosystem Framework

This root Lake configuration defines xLaDe as a meta-package.
It does not modify the Lean kernel and does not provide a monolithic library.
-/
package xLaDe where
  -- You are NOT a mathlib-style library
  -- This package mainly coordinates experiments, modes, and tooling
  moreServerOptions := #[
    ⟨`pp.universes, true⟩
  ]

/--
Lean dependency.

We intentionally avoid adding mathlib or other heavy dependencies
at the root level. Experiments may introduce their own dependencies.
-/
require lean from git
  "https://github.com/leanprover/lean4" @ "stable"

/--
Optional: a dummy library target so Lake is happy.
This is intentionally empty.
-/
@[default_target]
lean_lib xLaDe where
  roots := #[]
