# xLaDe Experiments

This directory contains **ecosystem-level experiments** for xLaDe.

An experiment in xLaDe is **not** a theorem, benchmark, or language extension.
Instead, it is a **controlled investigation** into how tooling, workflows,
policies, or user experience around Lean 4 can be structured, evaluated, and
improved — *without modifying Lean’s kernel or core semantics*.

Experiments are treated as **first-class research artifacts** and are orchestrated via the `xlade` CLI.

---

## What Is an Experiment?

An xLaDe experiment represents a **hypothesis about the Lean ecosystem**, such as:

- Can policy-based checks improve contributor experience?
- Can tooling changes surface more useful feedback to users?
- Can workflow conventions improve proof review discipline?
- Can orchestration layers exist without kernel modification?

Each experiment is designed to be:

- **Isolated** — no modification of Lean core or kernel
- **Reproducible** — discoverable and runnable via the CLI
- **Documented** — motivation, scope, and limits are explicit
- **Reversible** — experiments can be disabled or removed cleanly
- **Non-fatal** — failures inform evaluation rather than corrupting state

---

## Directory Structure

Each experiment lives in its own directory:

```
experiments/
  EXP-001/
    README.md
  EXP-002/
    README.md
```

The directory name serves as the **experiment identifier**, which is used by the CLI:

```
xlade list experiments
xlade run EXP-001
```

The CLI treats experiment directories as **opaque research units**; no hidden conventions are assumed beyond directory structure.

---

## Experiment Contents

Each experiment directory must contain at least:

* `README.md` — a complete description of the experiment

The README should document:

* the research question or hypothesis
* scope and affected components
* enforcement mechanism (if any)
* reversibility
* exit criteria

Additional files (scripts, configuration, notes, metrics) may be included as needed.

At the current stage, execution logic may be **lightweight or stubbed**.
This is intentional and reflects xLaDe’s research-first, interface-driven design.

---

## Lifecycle of an Experiment

Experiments follow a defined lifecycle (see `experiment-lifecycle.md`):

1. **Draft**
   Proposal and early exploration.

2. **Active**
   Controlled evaluation, typically enabled in Experimental Mode.

3. **Abandoned**
   Retired experiments preserved for historical and research context.

4. **Promoted**
   Successful ideas generalized into policies, tooling, or upstream proposals.

Lifecycle state must be declared explicitly by the experiment.

---

## Relationship to Modes

Experiment execution depends on the active xLaDe mode:

* **Experimental Mode**
  May enable Active experiments.

* **Stable Mode**
  Must not enable experiments.

* **Onboarding Mode**
  Must not enable experiments.

Mode selection controls *whether* experiments run; it does not change Lean behavior.

---

## Relationship to Lean Core

Experiments in xLaDe:

* ❌ do **not** modify Lean core
* ❌ do **not** alter kernel semantics
* ❌ do **not** require patched toolchains
* ✅ operate strictly at the ecosystem, tooling, or workflow level

Lean core is treated as **immutable infrastructure** and is included only as a reference baseline.

---

## Research Status

All experiments should be considered **experimental and evolving**.

They exist to:

* support research and learning,
* generate concrete artifacts for evaluation,
* and inform future tooling or policy design.

Stability, performance, and completeness are **explicitly not required**.

---

## Adding New Experiments

To add a new experiment:

1. Create a new directory under `experiments/`
2. Assign a unique identifier (e.g. `EXP-003`)
3. Add a `README.md` describing:

   * motivation and hypothesis
   * scope and enforcement
   * reversibility and exit criteria
4. Ensure the experiment is discoverable via:

   ```bash
   xlade list experiments
   ```

Community contributions are welcome, provided experiments respect kernel immutability and lifecycle discipline.

---

## Summary

xLaDe experiments provide a **structured, reversible framework** for exploring Lean ecosystem ideas.
They allow research into workflows, tooling, and policies while keeping Lean’s trusted core untouched and reproducible.
