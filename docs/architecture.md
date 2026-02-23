# xLaDe Architecture Overview

## 1. Purpose of This Document

This document describes the **architectural intent** of the xLaDe repository.  
xLaDe is an experimental, early-stage project that explores **ecosystem-level design considerations** around Lean 4, rather than introducing new formal results or kernel-level modifications.

The goal of this document is not to specify a finalized architecture, but to:
- make explicit which parts of the system are *stable* versus *experimental*,
- document boundaries for safe experimentation,

This document is intended for contributors, reviewers, and researchers who wish to understand how xLaDe is structured and how it is expected to evolve.

---

## 2. Architectural Philosophy

xLaDe is guided by three core architectural principles:

1. **Non-invasive experimentation**  
   Experiments should avoid modifying Lean’s trusted kernel or core semantics.

2. **Explicit architectural boundaries**  
   The repository should clearly distinguish between components that are fixed and components that may evolve.

3. **Minimal core with demand-driven growth**  
   New tooling or abstractions are introduced only in response to concrete use cases, rather than anticipated needs.

These principles prioritize clarity, reversibility, and long-term maintainability over rapid feature growth.

---

## 3. High-Level Repository Structure

At a high level, the xLaDe repository is organized as follows:

xLaDe/
|-- lean-core/               [trusted, immutable Lean 4 submodule]
|-- lean-toolchain           [pins Lean 4 version]
|-- lakefile.lean            [main build configuration]
|-- modes/                   [operational modes]
|   |-- stable/
|   |-- experimental/
|   |-- onboarding/
|-- experiments/             [isolated experiments]
|   |-- exp-001-proof-review/
|   |-- exp-002-kernel-boundary/
|-- policies/                [global constraints & lifecycle rules]
|-- xlade/                   [Python CLI orchestration package]
|-- scripts/                 [enforcement scripts]
|-- tools/                   [supporting utilities]
|-- docs/                    [architecture, rationale, roadmap]
|-- examples/                [minimal Lean demos]
|-- .github/                 [CI & contribution templates]
|-- LICENSE                  [GNU General Public License v3.0 (GPL-3.0)]

---

## 4. Architectural Boundaries

xLaDe distinguishes between **stable components** and **experimental components**.  
This separation is essential to ensure that ecosystem-level experimentation does not compromise correctness or upstream compatibility.

### 4.1 Stable Components (Do Not Modify)

- **Lean kernel and core semantics**  
  The trusted kernel and core type-theoretic semantics are treated as immutable.

- **Core compiler behavior**  
  Changes to elaboration, type checking, or evaluation semantics are out of scope.

These components are included via the `lean-core/` submodule to preserve provenance and simplify synchronization with upstream Lean.

---

### 4.2 Experimental Components (Safe to Explore)

- **Repository layout and organization**
- **Documentation structure**
- **Auxiliary tooling experiments**
- **Example overlays and prototype workflows**

These areas are the primary focus of xLaDe. Experiments here are expected to be lightweight, reversible, and well-documented.

---

## 5. The `lean-core/` Submodule

The `lean-core/` directory contains a forked snapshot of the Lean 4 core, tracked as a Git submodule.

The submodule serves two major purposes:

1. **Isolation**  
   Ecosystem-level experiments can be conducted without altering upstream code.

2. **Reversibility**  
   Updates or rollbacks are straightforward, avoiding long-lived divergence.

At the current stage, xLaDe does **not** introduce semantic changes to the Lean core.

---

## 6. Example Contribution Path (Conceptual)

A typical contribution to xLaDe may proceed as follows:

1. A contributor identifies a limitation or ecosystem-level pain point.
2. The idea is discussed via issues or documentation drafts.
3. A small, localized experiment is proposed (e.g., documentation layout, example workflow).
4. The experiment is evaluated informally.
5. If useful, it is integrated in a minimal and well-scoped form.

This workflow emphasizes **experimentation before commitment**.

---

## 7. Current Status and Limitations

xLaDe is currently in an exploratory and experimental phase.  
The repository should be understood as a research artifact rather than a production-ready ecosystem or tooling platform.

At this stage:

- No stable tools or finalized workflows are provided.
- No performance, scalability, or usability claims are made.
- Experiments remain limited in scope and qualitatively evaluated.
- All enforcement mechanisms operate at the repository level and are reversible.

This status is intentional. The project prioritizes clarity, explicit boundaries, and controlled experimentation over feature completeness. xLaDe is not intended to replace existing Lean workflows, but to document and evaluate ecosystem-level architectural choices.

---

## 8. Future Evolution

The architecture of xLaDe is expected to evolve incrementally.  
Future changes will be guided by experimental results, contributor feedback, and concrete use cases rather than speculative design.

Possible directions include:

- refinement of repository-level policies,
- extension of lightweight tooling,
- broader evaluation of workflow constraints,
- comparative ecosystem studies.

Growth is intended to remain demand-driven, with explicit justification for added complexity.

---

## 9. Summary

xLaDe treats ecosystem architecture as a first-class research object.  
Rather than introducing new proof technologies, it focuses on making architectural boundaries, workflow constraints, and repository-level policies explicit and testable.

By clearly distinguishing trusted infrastructure from experimental components, xLaDe provides a disciplined foundation for ecosystem-level experimentation around Lean 4. At its current stage, it serves as a structured starting point rather than a finished system.