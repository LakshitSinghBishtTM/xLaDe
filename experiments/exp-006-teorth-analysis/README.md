# EXP-006: Lean Companion to Analysis I

## Research Question

Can xLaDe wrap and build a Mathlib-dependent external Lean 4 project,
using that project's own build mechanism, with zero code connection to
xLaDe?

Every prior external-project experiment (EXP-004, EXP-005) is
dependency-free -- stdlib only. This is the first one that pulls in
Mathlib, which changes both the build mechanics (a cache-fetch step
becomes necessary) and the friction profile (bandwidth, disk space).

---

## Hypothesis

A Mathlib-dependent external Lean 4 repository, with no knowledge of
xLaDe, can be integrated as a submodule and built via its own provided
`build.sh` -- without modifying the project source, without building
Mathlib from source, and without touching the Lean kernel.

---

## Project

**Repository:** https://github.com/teorth/analysis
**Author:** Terence Tao (teorth)
**License:** Apache-2.0
**Submodule path:** `experiments/exp-006-teorth-analysis/analysis/`

Tao's own Lean 4 formalization of his textbook *Analysis I* -- a
paraphrasing of the book's definitions, theorems, and proofs (not
optimized for efficiency; exercises left to the reader are rendered as
`sorry`). Chapter 2 builds the natural numbers independently of Mathlib;
every chapter after that switches to Mathlib's definitions, so the
formalization is only partly self-contained by design.

**Coverage:** Chapters 2 through 11, plus two appendices on mathematical
logic and the decimal system (Chapter 1 is textbook introduction, not
formalized).

**Also in this repository, unrelated to the textbook, and built by the
same `lake build`:** an in-progress measure theory formalization,
physical units (including an SI system), a finite-choice formalization
avoiding Lean's axiom of choice, some finite probability theory, and
four solved Erdős problems.

**Dependencies:** Mathlib (the first xLaDe external-project experiment
with this dependency).

---

## Enforcement Mechanism

- Script-based: `scripts/experiments/run-exp-006.sh`
- Runs the project's own `./build.sh` inside the submodule, which does
  `lake exe cache get` (pulls Mathlib's prebuilt `.olean` cache) followed
  by `lake build`
- Exit code determines pass/fail

---

## Success Criteria

`compilation` -- `./build.sh` exits 0, meaning `lake exe cache get` and
`lake build` both succeeded.

Failure is any non-zero exit from `./build.sh`.

---

## Scope

- `experiments/exp-006-teorth-analysis/analysis/` -- the external project
- No modifications to xLaDe core, Lean kernel, or project source
- No scoping to just the textbook material -- `lake build` compiles
  everything in the repository, textbook and non-textbook content alike

---

## Non-Goals

- Does not test proof correctness beyond Lean's type checker
- Does not verify the textbook material builds independently of the
  non-textbook content (measure theory, physical units, etc.) -- a
  failure anywhere in the repository fails the whole run
- Does not modify the external project in any way
- Does not test all toolchain versions

---

## Reversibility

Remove the experiment directory and the submodule entry from
`.gitmodules`. No xLaDe core files are affected.

---

## Mode Integration

| Mode         | Status   |
|--------------|----------|
| Onboarding   | Disabled |
| Stable       | Disabled |
| Experimental | Enabled  |

---

## Relationship to EXP-004 / EXP-005

Both prior external-project experiments are dependency-free by design,
which kept the friction profile simple: install elan, populate the
submodule, run `lake build`. This one adds a real dependency graph and
a cache-fetch step in front of the build, which is a closer match to
what most real Lean projects actually look like -- most non-trivial
Lean work depends on Mathlib.

---

## Status

Active