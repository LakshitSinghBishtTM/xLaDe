# xLaDe CLI Demonstration

This document demonstrates **xLaDe as an executable ecosystem orchestration tool**.  
The CLI provides a **stable control surface** for experiments, policies, and metrics, while deliberately avoiding any modification of the Lean kernel or core semantics.

The purpose of this document is **illustrative**, not exhaustive.

---

## What the xLaDe CLI Is (and Is Not)

### The CLI **IS**
- An **orchestration layer** for ecosystem-level research artifacts
- A way to:
  - initialize project state
  - select ecosystem modes
  - discover experiments and metrics
  - run controlled ecosystem experiments
- A stable interface over evolving research components

### The CLI **IS NOT**
- A replacement for `lean` or `lake`
- A proof executor or elaboration engine
- A production-ready workflow or build system

Many execution backends are intentionally **lightweight or stubbed** at this stage.

---

## 1. Project Initialization

```
xlade init
```

### Effect

* Creates a project-local `.xlade/` directory
* Initializes runtime state files:

  * `experiments.lock`
  * `last-run`

### Purpose

* Marks the directory as an xLaDe workspace
* Enables experiment orchestration and state tracking

### Notes

* Safe to run multiple times
* Does not modify Lean source files or dependencies

---

## 2. Listing Available Experiments

```bash
xlade list experiments
```

### Effect

* Scans the `experiments/` directory
* Lists all discoverable experiment identifiers

### Example Output

```text
Available experiments:
  - EXP-001
  - EXP-002
```

### Purpose

* Makes ecosystem experiments visible
* Decouples experiment discovery from execution logic

At this stage, discovery is **structural**, not semantic.

---

## 3. Running an Experiment (Conceptual)

```
xlade run EXP-001
```

### Effect

* Validates that the workspace is initialized
* Records the experiment as the most recent run
* Invokes the experiment orchestration path

### Current Status

* Execution is **intentionally stubbed**
* The command establishes interface, lifecycle, and state flow

This allows experiment structure, policies, and metrics to be evaluated before committing to full execution backends.

---

## 4. Checking Workspace State

```bash
xlade status
```

### Effect

* Reports the last experiment run in the current workspace
* Reads project-local state from `.xlade/`

This command reports **history only**; it does not infer success or failure.

---

## 5. Environment Diagnostics

```bash
xlade doctor
```

### Effect

* Checks for required external tools (e.g. `lake`)
* Verifies presence of:

  * `lean-core/` submodule
  * `lean-toolchain`

### Purpose

* Helps diagnose setup issues
* Provides non-fatal, human-readable diagnostics

---

## 6. Ecosystem Modes (Overview)

```bash
xlade mode onboarding
xlade mode experimental
xlade mode stable
```

### Effect

* Sets the global xLaDe mode in `~/.xlade/`
* Influences:

  * which experiments are enabled
  * how strictly policies are enforced

Modes do **not** change Lean behavior directly; they control orchestration and policy layers only.

---

## Design Philosophy

The xLaDe CLI is intentionally:

* **Explicit** — no hidden behavior
* **Non-invasive** — Lean core remains untouched
* **Interface-first** — execution evolves behind stable commands
* **Research-oriented** — prioritizes clarity and reversibility over completeness

This enables disciplined ecosystem experimentation without risking upstream stability.

---

## Summary

The xLaDe CLI provides a **minimal but coherent execution narrative** for ecosystem-level research around Lean 4.

At this stage, its value lies in:

* making experiments discoverable,
* establishing lifecycle and state flow,
* and providing a concrete substrate for future tooling.

As experiments mature, execution backends may evolve — the CLI interface is designed to remain stable.
