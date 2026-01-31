# How to Read This Repository

This document explains **how to navigate and interpret the xLaDe repository**.

xLaDe is a research-oriented ecosystem framework. Not all directories are equal, and not all artifacts are intended to be fully implemented at this stage.

This guide is written for:
- reviewers
- examiners
- new contributors

---

## Where to Start

If you are new to xLaDe, read in this order:

1. `README.md`  
   High-level vision, scope, and non-goals.

2. `RESEARCH_SCOPE.md`  
   Academic framing and explicit boundaries.

3. `docs/CLI_DEMO.md`  
   How xLaDe is used conceptually.

4. `docs/RUNTIME_STATE.md`  
   How state is managed and isolated.

---

## Core Concepts

The core concepts of xLaDe are:

- **Modes** (`modes/`)  
  Express user intent (onboarding, experimental, stable).

- **Experiments** (`experiments/`)  
  First-class research artifacts testing ecosystem ideas.

- **Policies** (`policies/`)  
  Explicit constraints enforced via scripts or CI.

- **Metrics** (`metrics/`)  
  Observational artifacts for evaluation, not enforcement.

None of these modify Lean’s kernel or core semantics.

---

## What Is Intentionally Minimal

Some components are deliberately lightweight:

- CLI execution backends may be stubbed
- Metrics are qualitative
- Few experiments exist by design
- Lean code is minimal and illustrative

This reflects xLaDe’s **interface-first, research-first** philosophy.

---

## What Can Be Ignored on First Read

The following are not essential for understanding the core ideas:

- Placeholder Lean files
- Demo projects
- Draft experiments
- Incomplete tooling helpers

These exist to support exploration, not to define guarantees.

---

## What Is Enforced

Some constraints are **real and enforced**, not aspirational:

- Lean kernel immutability (CI enforced)
- Experiment isolation
- Mode-based experiment activation

These are central to xLaDe’s design.

---

## Summary

xLaDe should be read as a **research laboratory**, not a finished product.

Understanding the structure, boundaries, and intent matters more than counting features or lines of code.
