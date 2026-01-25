# xLaDe: Experimental Lean 4 Ecosystem Framework

![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Lean](https://img.shields.io/badge/Lean-4-blue)
![Contributors](https://img.shields.io/github/contributors/LakshitSinghBishtTM/xLaDe?color=green)
![Issues](https://img.shields.io/github/issues/LakshitSinghBishtTM/xLaDe)

**xLaDe** is an **experimental ecosystem framework built on top of Lean 4**.

Unlike traditional Lean repositories that focus on formalizing mathematics or verifying individual algorithms, **xLaDe explores how Lean is used** at the ecosystem level:

- repository structure  
- development workflows  
- governance and policy enforcement  
- experimentation with tooling and contributor practices  

xLaDe does **not modify the Lean kernel**.  
Instead, it provides a **distribution-like environment** around Lean with executable experiments, build modes, policies, metrics, and tooling.

---

## Current Version and Releases

- **Current version:** `v1.1.0`
- **Version file:** [`VERSION`](VERSION)

Release documentation:
- [`CHANGELOG.md`](CHANGELOG.md) — authoritative change history  
- [`RELEASES.md`](RELEASES.md) — archived GitHub release notes  

---

## Vision

xLaDe aims to provide a **safe, structured, and reproducible laboratory** for experimenting with Lean ecosystem ideas that are difficult to evaluate directly in upstream repositories.

The long-term vision includes exploration of:
- human-friendly proof workflows  
- improved onboarding and error understanding  
- tooling and workflow experiments  
- community-oriented development practices  

Importantly, xLaDe focuses on **ecosystem-level concerns**, not language-level changes or kernel modification.

For background and motivation, see:
- [`docs/WHY_xLaDe.md`](docs/WHY_xLaDe.md)

---

## What xLaDe Is (and Is Not)

### xLaDe **IS**
- a Lean-based **ecosystem experimentation platform**
- a framework for **workflow, governance, and tooling research**
- a repository with **executable and enforceable policies**
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
├── docs/                 Design rationale and architecture documents
├── examples/             Minimal Lean examples
├── experiments/          Executable ecosystem experiments
├── lean-core/            Lean 4 core (git submodule, immutable)
├── metrics/              Evaluation and metrics framework
├── modes/                Build modes (onboarding / experimental / stable)
├── policies/             Repository governance and rules
├── projects/             Minimal demo project
├── scripts/              Policy enforcement and helper scripts
├── tools/                Optional tooling
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

| Mode | Description |
|------|-------------|
| **Onboarding** | Learning-friendly, minimal enforcement |
| **Experimental** | Enables ecosystem experiments |
| **Stable** | Conservative defaults and strict policies |

Modes may influence:
- which experiments are enabled  
- policy enforcement behavior  
- stability expectations  

---

## Experiments

xLaDe treats **ecosystem ideas as first-class experiments**.

Each experiment:
- is isolated and reversible  
- has explicit scope  
- documents enforcement and evaluation  

Current experiments live under [`experiments/`](experiments/):

- **EXP-001 — Enforced Proof Review**  
  Lean-based policy requiring explicit review markers  

- **EXP-002 — Kernel Boundary Violation Detection**  
  CI-enforced protection against kernel modification  

Each experiment includes:
- `README.md` — description and rationale  
- `METRICS.md` — qualitative evaluation  

To propose a new experiment, use:
- [`experiments/EXPERIMENT_TEMPLATE.md`](experiments/EXPERIMENT_TEMPLATE.md)

---

## Metrics and Evaluation

xLaDe evaluates **ecosystem behavior**, not mathematical performance.

Metrics focus on:
- enforcement strength  
- scope of impact  
- developer friction  
- reversibility  
- governance clarity  

See:
- [`metrics/`](metrics/)  
- [`metrics/summary.md`](metrics/summary.md)

---

## Governance and Policies

Governance in xLaDe is **documented and enforced**.

- Policy definitions: [`policies/`](policies/)  
- Enforcement scripts: [`scripts/`](scripts/)  
- Automated checks: [`.github/workflows/`](.github/workflows/)  

Example enforced policy:
- Lean kernel immutability (`lean-core/` must not be modified)

---

## Reproducible Builds

xLaDe provides **reproducible builds by default**:

- [`lean-toolchain`](lean-toolchain) pins the Lean compiler version  
- [`lakefile.lean`](lakefile.lean) defines the root package  
- `lake-manifest.json` locks all resolved dependencies  

This ensures contributors and CI build **the same environment**.

---

## Installation

See:
- [`INSTALL.md`](INSTALL.md)

Quick start:

```bash
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
chmod +x bin/xlade
````

---

## Using xLaDe

xLaDe provides a lightweight CLI wrapper:

```bash
./bin/xlade onboarding
./bin/xlade experimental
./bin/xlade stable
```

The CLI is intentionally minimal and may evolve.

---

## xLaDe CLI

xLaDe provides a command-line interface to orchestrate Lean ecosystem
experiments, policies, and metrics.

---

### Commands

```text
xlade init
xlade mode <stable|experimental|onboarding>
xlade list experiments
xlade list policies
xlade run <experiment-id>
xlade check
xlade metrics
xlade status
xlade doctor
```

---

## Examples and Demo

* Minimal Lean examples: [`examples/`](examples/)
* Demo xLaDe project: [`projects/demo/`](projects/demo/)

---

## Contributing

Contributions are welcome — especially **new ecosystem experiments**.

Please read:

* [`CONTRIBUTING.md`](CONTRIBUTING.md)
* [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)

Contributions that modify the Lean kernel are **not accepted**.

---

## Security

For reporting vulnerabilities, see:

* [`SECURITY.md`](SECURITY.md)

---

## License

This project is open-source under the [Apache License 2.0](LICENSE).

---

## Project Status

xLaDe is **experimental**.

As of `v1.1.0`:

* the repository structure and governance framework are considered stable
* individual experiments may evolve, be promoted, or be retired

xLaDe exists as a **living laboratory** for Lean ecosystem design.

> ⚠️ **Note:** xLaDe is in an experimental stage. Features are evolving, and the ecosystem is designed for research, exploration, and collaboration. Your contributions help shape its future.
