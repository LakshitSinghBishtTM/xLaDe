# xLaDe Architecture Overview

## 1. Purpose of This Document

This document describes the **architectural intent** of the xLaDe repository.  
xLaDe is an experimental, early-stage project that explores **ecosystem-level design considerations** around Lean 4, rather than introducing new formal results or kernel-level modifications.

The goal of this document is not to specify a finalized architecture, but to:
- make explicit which parts of the system are *stable* versus *experimental*,
- document boundaries for safe experimentation,
- explain why the repository is intentionally minimal at its current stage.

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
├── lean-core/ # Forked snapshot of the Lean 4 core (submodule)
├── docs/ # Design documents and architectural notes
├── examples/ # Small exploratory examples (currently minimal)
├── .github/ # GitHub workflows and issue templates
├── .gitignore # Tells Git what NOT to track
├── .gitmodules # What it does and why xLaDe needs it
├── README.md # Project overview and scope
├── CONTRIBUTING.md # Contribution guidelines
├── CONTRIBUTORS.md # Contributors details
├── LICENSE # Open-source license


This structure is intentionally simple. The repository serves as a **conceptual and organizational scaffold** rather than a fully realized ecosystem.

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

The submodule serves three purposes:

1. **Provenance**  
   It makes explicit which version of Lean the repository is based on.

2. **Isolation**  
   Ecosystem-level experiments can be conducted without altering upstream code.

3. **Reversibility**  
   Updates or rollbacks are straightforward, avoiding long-lived divergence.

At the current stage, xLaDe does **not** introduce semantic changes to the Lean core.

---

## 6. Minimal Core and Demand-Driven Evolution

xLaDe intentionally avoids adding tooling, workflows, or abstractions in the absence of demonstrated need.  
This **minimal-core policy** is a deliberate design choice.

### Rationale:
- Avoid premature abstraction and feature bloat
- Reduce long-term maintenance overhead
- Keep the repository accessible to new contributors
- Allow design decisions to be informed by real usage patterns

Feature proposals are expected to emerge through:
- issues and discussions,
- small experimental branches,
- documented use cases or pain points.

Only after sufficient justification are changes incorporated into the main repository structure.

---

## 7. Example Contribution Path (Conceptual)

A typical contribution to xLaDe may proceed as follows:

1. A contributor identifies a limitation or ecosystem-level pain point.
2. The idea is discussed via issues or documentation drafts.
3. A small, localized experiment is proposed (e.g., documentation layout, example workflow).
4. The experiment is evaluated informally.
5. If useful, it is integrated in a minimal and well-scoped form.

This workflow emphasizes **experimentation before commitment**.

---

## 8. Current Status and Limitations

xLaDe is currently in an exploratory phase.  
At this stage:
- No stable tools or workflows are provided.
- No performance or usability claims are made.
- The repository primarily documents design intent and structural decisions.

This is intentional. The project is positioned as a **foundation for future exploration**, not as a finished ecosystem.

---

## 9. Future Evolution

As xLaDe evolves, this document will be updated to reflect:
- newly identified architectural constraints,
- validated workflows,
- lessons learned from experiments.

The architecture is expected to grow incrementally, guided by community feedback and concrete needs rather than speculative design.

---

## 10. Summary

xLaDe treats architecture as a first-class research object.  
By clearly stating what is fixed, what is experimental, and why the repository remains minimal, the project aims to support disciplined, transparent ecosystem-level experimentation around Lean 4.

