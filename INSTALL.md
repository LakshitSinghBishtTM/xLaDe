# Installing xLaDe

xLaDe is a **Lean-based ecosystem framework** for experimenting with tooling, policies, and workflows around Lean — without modifying Lean’s kernel or core semantics.
This document describes how to **clone and set up xLaDe locally** for experimentation and development.

---

## What This Installation Provides

Installing xLaDe gives you:

- a pinned Lean toolchain
- a reproducible repository layout
- access to ecosystem experiments, policies, and tooling
- the `xlade` CLI for orchestration

It does **not** replace the Lean toolchain or alter Lean behavior.

---

## Requirements

Before installing xLaDe, ensure the following are available:

- **Git**
- **Lean 4 toolchain**  
  https://leanprover.github.io/
- **Lake build tool**  
  (included with the Lean 4 toolchain)

You do not need any patched or forked versions of Lean.

---

## Quick Install

Clone the repository with submodules:

```
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

Optionally make the CLI executable:

```
chmod +x bin/xlade
```

This prepares the repository for local use.

---

## Lean Toolchain

xLaDe pins the Lean version via:

```
lean-toolchain
```

This ensures:

* reproducible builds
* consistent behavior across environments
* compatibility with experiments and policies

Lake will automatically use the pinned toolchain.

---

## Verifying the Installation

You can verify the setup using:

```
xlade doctor
```

This checks for:

* the Lean toolchain
* Lake availability
* required repository components

No changes are made during this check.

---

## Next Steps

After installation, you may want to:

```
xlade init
xlade mode experimental
xlade list experiments
```

Refer to the following documents for guidance:

* `docs/CLI_DEMO.md`
* `docs/RUNTIME_STATE.md`
* `modes/README.md`

---

## Uninstalling / Cleanup

xLaDe does not install system-wide components.

To remove xLaDe:

* delete the cloned repository
* optionally remove `~/.xlade/` to clear global state

This will not affect:

* your Lean installation
* existing Lean projects
* proof artifacts

---

## Summary

Installing xLaDe sets up a **self-contained, reproducible environment** for
ecosystem-level experimentation around Lean.

The installation process is intentionally minimal and reversible, reflecting
xLaDe’s research-first and non-invasive design philosophy.