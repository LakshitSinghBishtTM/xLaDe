# Reproducibility and Compatibility in xLaDe

## Background

Lean 4 is designed for rapid evolution. The core team prioritises
scalability and correctness over long-term backward compatibility. As a
result, Lean code written in earlier versions may not compile unchanged
in later versions. This is a known issue acknowledged by the Lean core
team — it is a deliberate trade-off, not an oversight.

---

## The Problem

This creates real challenges for anyone doing reproducible research with
Lean:

- An experiment that runs today may silently break next year
- Comparing results across Lean versions requires manual environment setup
- Preserving ecosystem-level research artifacts long-term is difficult
- Onboarding users working with older materials becomes progressively harder

In traditional workflows, these issues are handled manually — often
requiring ad-hoc fixes, migration effort, or simply abandoning old work.

---

## xLaDe's Approach

xLaDe does not attempt to modify Lean or enforce backward compatibility
at the language level. That is outside scope and would require forking
Lean itself.

Instead, xLaDe introduces a different model:

> **An experiment is defined by both its code and its environment.**

Each experiment records its full execution context as metadata. When xLaDe
runs an experiment, it has access to everything needed to reconstruct the
environment that experiment was written in — even years later.

This shifts the goal from **backward compatibility** (keeping old code
working in new environments) to **reproducibility** (being able to
reconstruct the old environment on demand). The distinction matters:
backward compatibility requires the language to stay stable, which Lean
cannot guarantee. Reproducibility requires good metadata and tooling,
which xLaDe can provide.

---

## Current Implementation — v1.5.0

As of v1.5.0, the reproducibility foundation is in place:

**Environment metadata via `experiment.toml`:**

Every experiment declares its required toolchain:

```toml
lean_toolchain = "leanprover/lean4:stable"
```

This is the first layer of the reproducibility record — what version of
Lean this experiment was designed to run against.

**Run metadata via `.xlade/metrics.json`:**

Every `xlade run` appends a structured record to `.xlade/metrics.json`:

```json
{
  "experiment_id": "exp-002-kernel-boundary",
  "experiment_name": "Kernel Boundary Violation Detection",
  "type": "script-policy",
  "mode": "experimental",
  "lean_toolchain": "leanprover/lean4:stable",
  "timestamp": "2026-05-26 14:10:03",
  "status": "success"
}
```

This creates a permanent audit trail — every run is associated with the
exact toolchain version and mode it executed in.

**Toolchain pinning:**

The `lean-toolchain` file in the repository root pins the Lean compiler
version used by the project. Combined with `lake-manifest.json` locking
dependencies, the build is reproducible from a clean clone.

---

## Planned Implementation

The current metadata recording is the foundation. The next stages build
on top of it:

**Stage 2 — Compatibility tracking:**
- Expanded `experiment.toml` schema: validated Lean versions, known
  breakages, last-tested date
- Compatibility matrix: which experiments pass on which Lean versions
- `xlade check` warns when the current Lean version differs from the
  experiment's validated version

**Stage 3 — Automated environment reconstruction:**
- `xlade run` automatically switches to the experiment's required
  toolchain via elan before executing
- No manual toolchain management needed
- Old experiments run against their original environment automatically

**Stage 4 — Long-term preservation:**
- Archive format for retired experiments
- Nothing deleted — everything traceable and re-runnable
- Experiments remain executable regardless of how much Lean has evolved
  since they were written

---

## Why Reproducibility Over Compatibility

Backward compatibility in a rapidly evolving language requires either
slowing development or maintaining multiple parallel versions of the
language indefinitely. Neither is acceptable for Lean.

Reproducibility requires only that the tooling can reconstruct a past
environment on demand. elan already supports installing and switching
between arbitrary Lean toolchain versions. The missing piece is the
metadata to know which environment to reconstruct — and xLaDe is building
exactly that.

This is a more honest solution to the problem. It does not pretend that
old code will always work in new environments. It ensures that old code
can always be run in its original environment.

---

## Summary

| Stage                                     | Status    | Description                               |
|-------------------------------------------|-----------|-------------------------------------------|
| Environment metadata in `experiment.toml` | ✅ Done   | Toolchain declared per experiment         |
| Run metadata in `metrics.json`            | ✅ Done   | Every run records toolchain and timestamp |
| Toolchain pinning via `lean-toolchain`    | ✅ Done   | Reproducible builds from clean clone      |
| Compatibility tracking and warnings       | 🔲 Future | Detect version mismatches                 |
| Automated environment reconstruction      | 🔲 Future | Auto-switch toolchain via elan            |
| Long-term experiment preservation         | 🔲 Future | Archive format, nothing deleted           |
 
Comments and feedback on this approach are welcome. Solving Lean 4's
reproducibility problem is one of xLaDe's core research goals, and
finding better approaches is part of the work.