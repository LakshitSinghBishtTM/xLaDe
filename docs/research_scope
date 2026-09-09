# Research Scope of xLaDe

## 1. Purpose of This Document

This document clarifies the **research scope, intent, and boundaries** of
the xLaDe project. It is written to prevent ambiguity regarding what the
project does and does not attempt to achieve.

xLaDe is a **research artifact**, not production software.

---

## 2. What xLaDe Is

xLaDe is an **experimental ecosystem framework built around Lean 4**,
designed to explore research questions related to:

- Reproducibility of formal verification experiments across Lean versions
- Tooling and automation around formal proofs
- Governance, policies, and lifecycle management in proof ecosystems
- Workflow design and policy enforcement without kernel modification
- Evaluation and metrics for ecosystem-level behaviour

The project focuses on **meta-level concerns** surrounding proof assistants
rather than extending mathematical libraries or modifying the Lean kernel.

---

## 3. What xLaDe Is Not

xLaDe explicitly does not:

- Modify the Lean 4 kernel, compiler, or trusted code base
- Claim performance or correctness improvements over Lean itself
- Replace existing Lean tooling or standard workflows
- Serve as a production-grade or community-supported platform
- Act as a fork of Lean 4
- Provide a mathlib-style library of formal mathematics

Lean 4 is treated strictly as an **external dependency**, not as a
component developed within this research.

---

## 4. Relationship to Lean 4

Lean 4 is included in this repository **only as a Git submodule**. This
design choice is intentional:

- Lean 4 remains an independently developed proof assistant
- xLaDe operates as an **overlay ecosystem** interacting with Lean through
  standard interfaces
- No changes are made to Lean's trusted computing base
- Any modification to the submodule is detected and rejected by CI

This separation ensures that all experimental results are attributable to
ecosystem-level design decisions, not core system modifications.

---

## 5. Research-Oriented Components

The repository is structured to mirror research concerns:

- `experiments/` — controlled experiments with explicit hypotheses and
  exit criteria
- `metrics/` — mechanisms for observing and evaluating ecosystem behaviour
- `modes/` — alternative operational modes (onboarding, experimental, stable)
- `policies/` — governance, contribution, and lifecycle rules
- `xlade/` — CLI orchestration layer, pip-installable
- `scripts/` — policy enforcement scripts
- `tools/` — auxiliary utilities supporting experimentation

These components collectively support investigation into **how proof
assistants are used**, not merely how proofs are written.

---

## 6. Current Scope

As of v1.5.0, xLaDe actively covers:

- CLI-based experiment orchestration
- Script-policy and lean-policy experiment execution
- Environment diagnostics and tooling checks
- Run history and structured metrics recording
- Kernel immutability enforcement via CI
- Build mode management
- 50+ automated tests across all CLI modules

---

## 7. Out of Scope — Now

The following are explicitly out of scope for the current stage:

- Large-scale formalization of mathematical theories
- Benchmarking against industrial proof workloads
- Long-term maintenance or backward compatibility guarantees
- IDE plugins or editor integrations
- GUI applications
- Multi-prover support (Coq, Isabelle, etc.)
- AI or language model integration
- Community forums or discussion infrastructure

These are not permanent exclusions. Several are long-term research
directions described in [`research_roadmap.md`](research_roadmap.md).
They are out of scope now because the foundation must be stable before
the structure can be built.

---

## 8. Out of Scope — Permanently

The following are permanently out of scope regardless of version:

- Modification of the Lean kernel or core semantics
- Forking Lean for xLaDe-specific language changes
- Replacing Lean's elaborator or type checker
- Competing with or superseding Lean's core development

These are not deferred — they are architectural constraints that define
what xLaDe is. Removing them would make xLaDe a different project.

---

## 9. Intended Audience

xLaDe is intended for:

- Researchers studying proof assistants, formal methods, and ecosystem design
- Students exploring experimental tooling around Lean 4
- Contributors interested in governance, reproducibility, and workflow research
- Anyone curious about how formal verification ecosystems can be structured and evaluated

It is not intended for general end users seeking a production proof
engineering environment, or for industrial deployment.

---

## 10. Summary

xLaDe is a **research-driven, exploratory ecosystem framework** investigating
how proof assistants like Lean 4 can be supported by better tooling,
evaluation methods, governance structures, and reproducibility mechanisms.

Its value lies in **structured experimentation and honest evaluation**, not
in production readiness or adoption metrics. It exists to find out what
works — and to document what does not.