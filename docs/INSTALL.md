# Installing xLaDe

This document describes how to install xLaDe and all of its dependencies
from scratch. Follow the steps in order.

---

## Overview

xLaDe has two independent dependency stacks:

- **Lean toolchain** — required to run Lean-policy experiments (EXP-001)
- **Python package** — required to use the `xlade` CLI

You need both. The Lean toolchain takes longer to install; the Python
package installs in seconds.

---

## System Requirements

| Requirement | Minimum        | Notes                                  |
|-------------|----------------|----------------------------------------|
| OS          | Linux / macOS  | Windows via WSL2 is supported          |
| CPU         | x86_64 / ARM64 | Apple Silicon (M1/M2/M3) is supported  |
| RAM         | 4 GB           | 8 GB recommended for lake build        |
| Disk        | 2 GB free      | Lean toolchain is ~500 MB              |
| Python      | 3.11+          | 3.12 or 3.14 recommended               |
| Git         | Any recent     | Required by lake for package fetching  |

---

## Part 1 — Lean Toolchain

### Step 1.1 — Install elan

elan is the Lean version manager. It installs and manages Lean toolchains
and places the `lean`, `lake`, and `elan` binaries on your PATH.

> **Do not install lean or lake directly via your system package manager
> (e.g. `apt install elan` or `brew install lean`). These are outdated
> and will not work correctly with xLaDe.**

**Linux / macOS / WSL2:**

```sh
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
```

When prompted:

- Press **Enter** to accept the default installation path (`~/.elan`)
- Choose **1** to allow elan to modify your shell config automatically

After the installer finishes, either restart your terminal or run the
command it prints to update your current shell session (typically
`source ~/.elan/env`).

**macOS (Homebrew alternative):**

```sh
brew install elan-init
```

**Verify elan is installed:**

```sh
elan --version
```

Expected output:

```
elan 3.x.x (...)
```

---

### Step 1.2 — Install the Lean toolchain

elan reads the `lean-toolchain` file in the xLaDe directory to know which
Lean version to use. Clone the repository first (Part 2, Step 2.1), then
return here.

From inside the xLaDe directory, run:

```sh
elan toolchain install leanprover/lean4:stable
```

elan will download the Lean compiler and lake. This may take a few minutes
depending on your connection speed (~500 MB download).

**Verify lean is available:**

```sh
lean --version
```

Expected output:

```
Lean (version 4.x.x, ...)
```

**Verify lake is available:**

```sh
lake --version
```

Expected output:

```
Lake version 4.x.x (Lean version 4.x.x)
```

---

### Step 1.3 — Verify the toolchain in context

From inside the xLaDe directory:

```sh
elan show
```

You should see `leanprover/lean4:stable` listed as the active toolchain,
overridden by the `lean-toolchain` file in the project directory.

---

## Part 2 — xLaDe Repository

### Step 2.1 — Clone the repository

Clone with submodules. The `lean-core` submodule is required.

```sh
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

If you already cloned without `--recurse-submodules`, initialise the
submodule manually:

```sh
git submodule update --init --recursive
```

---

## Part 3 — Python CLI

### Step 3.1 — Create a virtual environment (recommended)

```sh
python3 -m venv venv
source venv/bin/activate
```

On Windows (WSL2 users can skip this):

```sh
python3 -m venv venv
venv\Scripts\activate
```

---

### Step 3.2 — Install xlade

```sh
pip install -e .
```

This installs xLaDe in editable mode. The `xlade` command will be
available in your active environment immediately.

**Verify the CLI is installed:**

```sh
xlade --help
```

Expected output:

```
xLaDe — Experimental Lean Ecosystem Orchestrator

Usage:
  xlade init
  xlade mode <stable|experimental|onboarding>
  xlade list experiments
  ...
```

---

## Part 4 — Verify the Full Installation

Run the built-in diagnostics:

```sh
xlade doctor
```

A fully working installation produces:

```
xLaDe Doctor Report
===================

✅ elan found
✅ lake found
✅ lean-core submodule present
✅ lean-toolchain present  (leanprover/lean4:stable)
⚠️  workspace not initialised

✅ All checks passed. xLaDe environment looks good.
```

The workspace warning is expected on a fresh clone. Fix it with:

```sh
xlade init
```

Then run `xlade doctor` again — all items should show ✅.

---

## Part 5 — Run the Test Suite

Confirm everything is working end to end:

```sh
pip install pytest
pytest tests/ -v
```

All tests should pass. The suite does not require a live Lean installation
to run.

---

## Part 6 — First Experiment

```sh
xlade mode experimental
xlade list experiments
xlade run EXP-002
```

EXP-002 (Kernel Boundary Violation Detection) runs without Lake and is a
good first experiment to verify the CLI is functional.

EXP-001 (Enforced Proof Review) requires Lake to be installed and will
report `skipped` if it is not. Complete Part 1 first.

---

## Troubleshooting

### `xlade: command not found`

The virtual environment is not active, or the package was not installed.

```sh
source venv/bin/activate
pip install -e .
```

### `lake not found` after installing elan

Your shell config was not reloaded after the elan install. Run:

```sh
source ~/.elan/env
```

Or restart your terminal.

### `lean-core missing` from `xlade doctor`

The submodule was not initialised. Run:

```sh
git submodule update --init --recursive
```

### `apt` or system package manager suggests `sudo apt install elan`

Ignore this. The system package is outdated and not compatible with
xLaDe. Use the `curl` installer from Step 1.1.

### Slow or failed Lean toolchain download

The Lean toolchain is large (~500 MB). On a slow connection, the download
may time out. Re-run:

```sh
elan toolchain install leanprover/lean4:stable
```

elan will resume from where it left off.

---

## Uninstalling

**Remove xLaDe:**

```sh
cd ..
rm -rf xLaDe
```

**Remove the Lean toolchain:**

```sh
elan toolchain uninstall leanprover/lean4:stable
```

**Remove elan entirely:**

```sh
elan self uninstall
```

This removes `~/.elan` and reverts any PATH changes elan made to your
shell config.

**Remove the Python virtual environment:**

```sh
rm -rf venv
```

---

## See Also

- [`docs/CLI_DEMO.md`](docs/CLI_DEMO.md) — CLI usage walkthrough
- [`docs/END_TO_END_TRACE.md`](docs/END_TO_END_TRACE.md) — full usage trace
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution guidelines
- [elan repository](https://github.com/leanprover/elan) — elan source and releases
- [Lean 4 installation guide](https://lean-lang.org/install/manual/) — official Lean docs