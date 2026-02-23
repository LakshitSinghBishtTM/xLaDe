# xLaDe: Experimental Lean 4 Ecosystem Framework

![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)
![Version](https://img.shields.io/badge/version-1.2.0-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Lean](https://img.shields.io/badge/Lean-4-blue)
![Contributors](https://img.shields.io/github/contributors/LakshitSinghBishtTM/xLaDe?color=green)
![Issues](https://img.shields.io/github/issues/LakshitSinghBishtTM/xLaDe)

**xLaDe** is an experimental Lean 4 ecosystem framework for studying tooling, workflows, governance, and policy enforcement in a controlled, reproducible environment. It is free and open-source software (FOSS), released under the GNU General Public License v3.0.

Unlike traditional Lean repositories that focus on formalizing mathematics or verifying individual algorithms, **xLaDe explores how Lean is used** at the *ecosystem level*:

- repository structure
- development workflows
- governance and policy enforcement
- experimentation with tooling and contributor practices

xLaDe does **not** modify the Lean kernel.
Instead, it provides a controlled, distribution-like environment around Lean with executable experiments, build modes, policies, metrics, and tooling.

---

## How to Read This Repository

This repository is intentionally broad and research-oriented.

Start here:
- [`HOW_TO_READ_THIS_REPO.md`](HOW_TO_READ_THIS_REPO.md)

Known limitations:
- [`LIMITATIONS.md`](LIMITATIONS.md)

Security and boundary assumptions:
- [`THREAT_MODEL.md`](THREAT_MODEL.md)

---

## Current Version and Releases

- **Current version:** `v1.2.0`
- **Version file:** [`VERSION`](VERSION)

Release documentation:
- [`CHANGELOG.md`](CHANGELOG.md)
- [`RELEASES.md`](RELEASES.md)

---

## Vision

xLaDe aims to provide a **safe, structured, and reproducible laboratory** for experimenting with Lean ecosystem ideas that are difficult to evaluate directly in upstream repositories.

The long-term vision includes exploration of:
- human-friendly proof workflows
- improved onboarding and error understanding
- tooling and workflow experiments
- community-oriented development practices

xLaDe focuses strictly on **ecosystem-level concerns**, not language-level changes or kernel modification.

For motivation, see:
- [`docs/WHY_xLaDe.md`](docs/WHY_xLaDe.md)

---

## What xLaDe Is (and Is Not)

### xLaDe **IS**
- a Lean-based **ecosystem experimentation platform**
- a framework for **workflow, governance, and tooling research**
- a repository with **documented and enforced policies**
- a safe environment for experimentation **without upstream disruption**

### xLaDe **IS NOT**
- a new theorem prover
- a replacement for Lean
- a modified Lean kernel
- a mathlib-style library

---

## Repository Structure

```
xLaDe/
├── .github/              CI workflows and GitHub automation
├── bin/                  xLaDe CLI entrypoint (xlade)
├── docs/                 Design rationale and usage documentation
├── examples/             Minimal Lean examples
├── experiments/          Ecosystem experiments
├── lean-core/            Lean 4 core (git submodule, immutable)
├── metrics/              Evaluation and metrics framework
├── modes/                Build modes (onboarding / experimental / stable)
├── policies/             Repository governance and rules
├── projects/             Minimal demo project
├── scripts/              Policy enforcement scripts
├── tools/                Optional helper tools
├── lakefile.lean         Root Lake configuration
├── lake-manifest.json    Locked dependency graph (generated)
├── lean-toolchain        Pinned Lean compiler version
├── INSTALL.md            Installation instructions
├── SECURITY.md           Security disclosure policy
├── CODE_OF_CONDUCT.md    Community code of conduct
├── CONTRIBUTING.md       Contribution guidelines
├── CONTRIBUTORS.md       Contributor acknowledgements
├── LICENSE               License information
├── README.md             Project overview
└── VERSION               Current version
````

---

## Build Modes

xLaDe supports **multiple build modes**, reflecting different user intents.

Defined under [`modes/`](modes/):

| Mode             | Description                               |
| ---------------- | ----------------------------------------- |
| **Onboarding**   | Learning-friendly, minimal enforcement    |
| **Experimental** | Enables ecosystem experiments             |
| **Stable**       | Conservative defaults and strict policies |

Modes may influence:

* which experiments are enabled
* policy enforcement behavior
* stability expectations

---

## Experiments

xLaDe treats **ecosystem ideas as first-class experiments**.

Each experiment:

* is isolated and reversible
* has explicit scope and lifecycle
* documents enforcement and evaluation

See:

* [`experiments/`](experiments/)
* [`experiments/EXPERIMENT_TEMPLATE.md`](experiments/EXPERIMENT_TEMPLATE.md)

---

## Metrics and Evaluation

xLaDe evaluates **ecosystem behavior**, not mathematical performance.

Metrics focus on:

* enforcement strength
* developer friction
* reversibility
* governance clarity

See:

* [`metrics/`](metrics/)
* [`metrics/summary.md`](metrics/summary.md)

---

## Governance and Policies

Governance in xLaDe is **explicit and enforceable**.

* Policies: [`policies/`](policies/)
* Enforcement scripts: [`scripts/`](scripts/)
* Automated checks: [`.github/workflows/`](.github/workflows/)

Kernel immutability is enforced via CI.

---

## Reproducible Builds

xLaDe provides **reproducible builds by default**:

* [`lean-toolchain`](lean-toolchain) pins Lean
* [`lakefile.lean`](lakefile.lean) defines the root package
* `lake-manifest.json` locks dependencies

---

## Installation

See:

* [`INSTALL.md`](INSTALL.md)

---

## Using xLaDe

xLaDe provides a lightweight CLI for orchestration:

```
xlade init
xlade mode experimental
xlade list experiments
xlade run EXP-001
```

See:

* [`docs/CLI_DEMO.md`](docs/CLI_DEMO.md)
* [`docs/END_TO_END_TRACE.md`](docs/END_TO_END_TRACE.md)

---

## Contributing

Contributions are welcome — especially **new ecosystem experiments**.

See:

* [`CONTRIBUTING.md`](CONTRIBUTING.md)
* [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)

Contributions that modify the Lean kernel are **not accepted**.

---

## License

Copyright (C) 2026 Lakshit Singh Bisht

This project is licensed under the GNU General Public License v3.0. See LICENSE for details.

```Note: This project depends on Lean 4, which is licensed under the Apache License 2.0 and is included unmodified.```

---

## Project Status

xLaDe is **experimental**.

As of `v1.2.0`:

* repository structure and governance are stable
* experiments may evolve, be promoted, or retired
* cli based app may be unstable

xLaDe exists as a **living laboratory** for Lean ecosystem design.
