# How to Read This Repository

This document explains how to navigate and interpret the xLaDe repository. Not all directories are equal, and not all artifacts are intended to be fully implemented at this stage. This guide is specially for new contributors.

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

## Intentionally Minimal Components

- CLI execution
- Qualitative metrices
- Few experiments
- Lean code

---

## Files to Ignore

- Placeholder Lean files
- Demo project
- Incomplete tooling

---

## What Is Enforced

- Lean kernel immutability (CI enforced)
- Experiment isolation
- Mode-based experiment activation

---

xLaDe should be read as a research laboratory, not a finished product. Understanding the structure, boundaries, and intent matters more than counting features or lines of code.