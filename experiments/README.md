# xLaDe Experiments

This directory contains **ecosystem-level experiments** for xLaDe.

An experiment in xLaDe is **not** a theorem or a benchmark. Instead, it is a
controlled investigation into how tooling, workflows, policies, or user
experience around Lean 4 can be structured, evaluated, and improved.

Experiments are treated as **first-class research artifacts** and are
orchestrated by the `xlade` CLI.

---

## What Is an Experiment?

An xLaDe experiment represents a **hypothesis about the Lean ecosystem**, such
as:

- Can certain workflows improve proof readability?
- Can policy-based checks improve contributor experience?
- Can tooling changes surface more useful feedback to users?
- Can orchestration layers exist without modifying Lean core?

Each experiment is designed to be:

- **Isolated** — experiments do not modify Lean core
- **Reproducible** — experiments can be discovered and executed via the CLI
- **Documented** — each experiment explains its motivation and scope
- **Non-fatal** — failures produce information, not hard errors

---

## Directory Structure

Each experiment lives in its own directory:

```text
experiments/
  EXP-001/
    README.md
  EXP-002/
    README.md
````

The directory name serves as the **experiment identifier**, which is used by the
CLI:

```bash
xlade list experiments
xlade run EXP-001
```

---

## Experiment Contents

Each experiment directory should contain at least:

* `README.md` — description of the experiment

Additional files (scripts, configuration, notes) may be added as needed by the
experiment.

At the current stage, execution logic may be **lightweight or stubbed**. This is
intentional and reflects the research-first nature of the project.

---

## Lifecycle of an Experiment

1. **Proposal**
   The experiment is introduced with a clear motivation and scope.

2. **Orchestration**
   The experiment becomes discoverable and runnable via the xLaDe CLI.

3. **Evaluation**
   Metrics, policies, or observations are collected and analyzed.

4. **Outcome**
   Results may inform tooling changes, policy refinements, or future research.
   Successful ideas may later be proposed upstream or implemented more fully.

---

## Relationship to Lean Core

Experiments in xLaDe:

* ❌ Do **not** modify Lean core
* ❌ Do **not** redefine kernel behavior
* ✅ Operate at the ecosystem, tooling, or workflow level

Lean core is treated as **immutable infrastructure** and is included only as a
reference baseline.

---

## Research Status

All experiments should be considered **experimental and evolving**.

They are intended to:

* support research and learning,
* guide future development directions,
* and provide concrete artifacts for evaluation and discussion.

Stability, performance, and completeness are **explicitly not required** at this
stage.

---

## Adding New Experiments

To add a new experiment:

1. Create a new directory under `experiments/`
2. Assign a unique identifier (e.g., `EXP-003`)
3. Add a `README.md` describing:

   * motivation
   * scope
   * expected outcomes
4. Ensure the experiment can be discovered via `xlade list experiments`

Community contributions are welcome.
