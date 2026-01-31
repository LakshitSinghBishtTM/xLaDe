# xLaDe Runtime State

This document describes how **xLaDe manages runtime state** across user environments and individual projects.

xLaDe separates state into **global state** (user-level preferences and modes) and **project-local state** (experiment execution and history).  
This separation is intentional and supports reproducibility, isolation, and clarity.

---

## Design Principles

xLaDe runtime state is designed to be:

- **Explicit** — all state is stored in visible files and directories
- **Non-invasive** — no Lean core or project source files are modified
- **Minimal** — only essential orchestration state is recorded
- **Recoverable** — deleting state resets behavior without breaking projects

No runtime state affects Lean’s kernel, semantics, or proof behavior.

---

## Global State

Global state is stored in the user’s home directory:

```text
~/.xlade/
````

This directory contains **user-wide configuration and mode selection**.

### Contents

```text
~/.xlade/
├── config.toml
├── mode
└── runs/
```

#### `config.toml`

* Stores user-level configuration options
* Intended for:

  * future CLI preferences
  * default behaviors
  * Optional; absence does not prevent xLaDe usage

#### `mode`

* Stores the currently active xLaDe mode:

  * `onboarding`
  * `experimental`
  * `stable`

* Set via:

  ```bash
  xlade mode <mode>
  ```

* Influences:

  * which experiments are enabled
  * how strictly policies are enforced

This file does **not** alter Lean itself.

#### `runs/`

* Reserved directory for future experiment execution records
* Intended to support:

  * global summaries
  * cross-project analysis
  * May be empty at early stages

---

## Project-Local State

Project-local state is stored inside the project directory:

```text
.xlade/
```

This directory is created by:

```bash
xlade init
```

It marks the directory as an **xLaDe workspace**.

### Contents

```text
.xlade/
├── experiments.lock
├── metrics.json
└── last-run
```

#### `experiments.lock`

* Records experiment-related state
* Intended to support:

  * reproducibility
  * controlled experiment activation
  * Human-readable and manually inspectable

#### `metrics.json`

* Stores metrics generated or referenced by experiment runs
* May be:

  * empty
  * partial
  * qualitative
  * Metrics are **observational**, not enforcement mechanisms

Missing or incomplete metrics never cause execution failure.

#### `last-run`

* Records the identifier of the most recently executed experiment
* Used by:

  ```bash
  xlade status
  ```
* If unset or empty, no experiment has been run yet

---

## Lifecycle and Cleanup

* Deleting `.xlade/` resets project-local xLaDe state
* Deleting `~/.xlade/` resets user-wide xLaDe state
* Neither operation affects:

  * Lean source files
  * proof artifacts
  * build outputs

This makes experimentation **safe and reversible**.

---

## Summary

xLaDe runtime state exists solely to support **ecosystem orchestration**.

It:

* tracks modes and experiment history,
* enables reproducible experimentation,
* and avoids entanglement with Lean’s trusted core.

Runtime state is intentionally minimal and transparent, reflecting xLaDe’s research-first and non-invasive design philosophy.
