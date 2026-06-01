# xLaDe Overview

**xLaDe** is an experimental ecosystem framework built around **Lean 4**,
designed to enable controlled experimentation with tooling, workflows,
governance, and policy enforcement **without modifying Lean core**.

Rather than being a theorem library or a replacement for Lean, xLaDe acts as an
**orchestration layer**. It provides a structured way to run ecosystem
experiments, apply policies, collect metrics, and evolve tooling ideas in a
reproducible and reviewable manner.

xLaDe is delivered as a **pip-installable CLI application** (`xlade`). This
CLI-first approach establishes stable interfaces on top of which richer
execution engines, IDE integrations, and GUI-based tooling can be developed
in later stages.

---

## Why xLaDe

Lean 4 has two ecosystem-level problems that xLaDe is designed to address.

**Backward compatibility.** Proofs written in Lean 4 are tied to the version
they were written in. Something that compiles today may break silently next
year as Lean evolves. xLaDe's approach is to record full environment metadata
with every experiment — toolchain version, dependencies, execution context —
so experiments can be reconstructed and re-executed correctly even years later.
Reproducibility instead of compatibility.

**Kernel drift.** When a project builds directly on top of a Lean fork, it
gradually diverges from upstream. One day it breaks with no clear record of
what was keeping it stable. xLaDe treats the Lean kernel as immutable
infrastructure — locked as a Git submodule, with any modification detected
and rejected by CI automatically. Experiments operate strictly above Lean,
never inside it.

For the full rationale, see [`WHY_xLaDe.md`](WHY_xLaDe.md).

---

## Current Status

xLaDe is in a **functional experimental stage** as of `v1.5.0`.

The project currently provides:

- A **pip-installable CLI** (`xlade`) for ecosystem orchestration
- **Real experiment execution** — EXP-002 and EXP-003 run via subprocess,
  EXP-001 runs when Lake is installed
- **Actionable environment diagnostics** — `xlade doctor` identifies missing
  tools and prints the exact commands to fix them
- **Run history and metrics** — structured JSON written on every experiment
  run, displayed via `xlade status` and `xlade metrics`
- **Build modes** — onboarding, experimental, and stable with different
  enforcement levels
- **Kernel immutability** enforced via CI
- **50+ test pytest suite**, all passing on Python 3.11–3.14
- **Cross-platform** — Built for Linux x86\_64, Windows, MacOS, and Android aarch64
  (Termux)

---

## Project Vision

xLaDe aims to support a modern, flexible, and extensible Lean 4 ecosystem
that prioritizes **human-centered formal reasoning** and experimental
innovation.

The long-term vision includes:

- **Reproducible experiment environments** — run any experiment against its
  original Lean version, years after it was written
- **Human-readable proof workflows** — improved tactics, humanized error
  explanations, and corrective guidance
- **AI-assisted theorem proving** — integration of large language models for
  proof assistance, error diagnosis, and proof translation
- **Cross-prover experimentation** — support for Coq, Isabelle, and other
  proof assistants alongside Lean
- **IDE and GUI tooling** — richer interfaces built on top of the stable CLI
- **Interoperability** — experiments that bridge multiple proof assistants
- **Community-driven development** — tooling and workflows designed around
  how people actually work with formal proofs

xLaDe does not attempt to replace Lean or compete with its core development.
It provides a structured environment in which ecosystem ideas can be tested,
evaluated, and iterated upon — and potentially proposed upstream.

---

## Getting Involved

Contributions are welcome at all levels — experiments, documentation,
tooling, and feedback.

- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — how to contribute
- [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) — community standards
- GitHub Issues — bug reports, feature proposals, discussions

---

## Further Reading

| Document                                      | Description                               |
|-----------------------------------------------|-------------------------------------------|
| [`WHY_xLaDe.md`](WHY_xLaDe.md)                | Detailed motivation and design rationale  |
| [`architecture.md`](architecture.md)          | Architectural boundaries and philosophy   |
| [`RESEARCH_SCOPE.md`](RESEARCH_SCOPE.md)      | Research scope and explicit non-goals     |
| [`roadmap.md`](roadmap.md)                    | Release roadmap                           |
| [`CLI_DEMO.md`](CLI_DEMO.md)                  | Complete CLI command reference            |
| [`END_TO_END_TRACE.md`](END_TO_END_TRACE.md)  | Full session walkthrough with real output |
| [`../INSTALL.md`](../INSTALL.md)              | Installation guide                        |