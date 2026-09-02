import Lake
open Lake DSL

package xLaDe where
  moreServerOptions := #[
    ⟨`pp.universes, true⟩
  ]

/-
  # In simple language, what it says ---
  # This repository is called xLaDe, and Lake manages it as a Lean project.
  # Do not build anything at the repository root.
-/
