# End-to-End Usage Trace

This document provides a **narrative execution trace** showing how xLaDe is intended to be used from start to finish.
This is not a tutorial, but a conceptual walkthrough.

---

## Scenario

A researcher wants to evaluate whether proof review discipline can be enforced without modifying the Lean kernel.

---

## Step 1: Clone and Inspect

```
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

The repository includes:

* Lean core as a submodule
* experiments and policies
* xLaDe CLI

## Step 2: Initialize Workspace

```
xlade init
```

Creates a .xlade/ directory for project-local state.
No Lean files are modified.

## Step 3: Select Mode

```
xlade mode experimental
```

This enables experimental behavior without affecting Lean semantics.

## Step 4: Discover Experiments

```
xlade list experiments
```

Shows available ecosystem experiments.

## Step 5: Run an Experiment

```
xlade run EXP-001
```

Validates workspace state
Records execution
Applies experiment orchestration logic

Execution may be stubbed, but lifecycle and state flow are established.

## Step 6: Inspect State

```
xlade status
```
Reports the last executed experiment.

## Step 7: Cleanup or Disable

```
rm -rf .xlade
```
Note:
This command removes only xLaDe’s project-local state directory.
Do NOT run ```sudo rm -rf /``` 

Effect:

* Resets all project-local xLaDe state
* Lean source files and kernel remain untouched 

## Summary
This trace demonstrates that xLaDe orchestrates ecosystem experiments, records state explicitly, and remains reversible and non-invasive.
