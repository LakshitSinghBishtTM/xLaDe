# xLaDe Demo Project

This directory contains a **minimal demonstration project** showing how xLaDe is intended to be used with an existing Lean repository structure.
The demo focuses on **ecosystem orchestration**, not on proof content or Lean language features.

---

## Purpose of the Demo

The demo project exists to:

- illustrate how xLaDe is invoked from a repository
- demonstrate experiment orchestration using in-repo experiments
- provide a concrete, low-friction example for contributors and reviewers

It is **not** intended to showcase advanced Lean proofs or production workflows.

---

## Prerequisites

Before running the demo, ensure that:

- xLaDe has been initialized in the repository
- the `xlade` CLI is executable
- experiments are available in the `experiments/` directory

```
chmod +x bin/xlade
````

---

## Running the Demo (Conceptual)

From the **repository root**, run:

```
xlade init
xlade mode experimental
xlade run EXP-001
```

### What This Does

* Initializes a project-local `.xlade/` workspace
* Enables Experimental Mode
* Orchestrates the selected ecosystem experiment

At the current stage:

* experiment execution may be **stubbed**
* the command establishes lifecycle, state flow, and orchestration semantics

This is intentional and reflects xLaDe’s research-first design.

---

## Relationship to In-Repo Experiments

This demo intentionally uses **experiments defined within the same repository**.

This ensures that:

* no external dependencies are required
* experiment structure remains visible and inspectable
* behavior is reproducible for reviewers and contributors

---

## Version Control Context

This demo project is tracked in version control to:

* provide a stable reference example
* ensure documentation remains reproducible
* support review and discussion

Example setup commands:

```
mkdir -p projects/demo
touch projects/demo/README.md
git add projects/demo/README.md
git commit -m "Add simple xLaDe demo project"
git push
```

---

## Summary

The xLaDe demo project provides a **minimal, concrete usage narrative** for the
xLaDe ecosystem.

Its goal is not feature completeness, but **clarity**:

* how xLaDe is invoked,
* how experiments are selected,
* and how orchestration state is managed.

More complex examples may be added as xLaDe evolves.