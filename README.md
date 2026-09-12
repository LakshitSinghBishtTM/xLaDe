<p align="center">
  <img alt="xLaDe Logo"
       src="assets/logo/xlade-logo.svg"
       width="260">
</p>

<h1 align="center">xLaDe</h1>
<p align="center">eXperimental Lean 4 advanced Development ecosystem</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.8.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/status-experimental-red" alt="Status">
  <img src="https://img.shields.io/badge/platform-Linux-green" alt="Platform">
  <img src="https://img.shields.io/badge/Lean-4-purple" alt="Lean 4">
</p>

---

xLaDe is a simple Python-based CLI tool built for executing and preserving Lean 4 projects. It is an ecosystem-level tool, which records the toolchain and other metadata of projects and allows the reconstruction and rebuilding of that exact environment later. 

Lean 4 undergoes rapid development, which can introduce backward-compatibility issues. This problem becomes more difficult as the versions accumulate over time. xLaDe is built to mitigate the practical issues of backward-compatibility problems and improve ecosystem-level tooling for the Lean 4 theorem prover. 

Instead of directly solving backward-compatibility issues by storing every version of Lean 4 and other tools or providing cross-version compatibility, xLaDe tries to store sufficient environment metadata such as toolchains, dependencies, and other context, and then recreates the environment for running Lean 4 projects upon request, also termed as experiments in xLaDe. In this process, xLaDe does not interfere with Lean 4 work and doesn't change anything in Lean 4 projects. It sits on a layer above Lean 4 and there are no modifications to other layers.

xLaDe treats the Lean 4 kernel as immutable and provides CI-based checks to prevent modifications to Lean 4. The Lean 4 repository is included in xLaDe as a submodule and remains optional for use. xLaDe is an opinionated tool, and its policies are enforced by workflows and scripts rather than simply being documented.

---

## Why not to use xLaDe

- xLaDe is still being actively developed and updated 
- Tools, metrics, etc. modules are not yet fully implemented
- The installation process may be difficult for beginners
- It may be unintuitive for non-Linux users
- It is a boring tool, there is no groundbreaking magic
- The use cases are primarily focused on long-term reproducibility, so it may feel less useful initially 

---

## Features

- Experiments runnable via xLaDe CLI
- Modes controlling experiment execution
- Comprehensive environment metadata for Lean 4 projects
- Immutability of Lean 4 kernel via CI workflows
- Comprehensive documentation and governance model
- Security measures according to the documented threat model 
- Optimised and lightweight
 
---

## Quick Start
 
To install the entire project:

```sh
git clone https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
python -m venv venv
source venv/bin/activate
pip install .
xlade
```

To install the core CLI only, without experiments and other modules:

```sh
pip install xlade
xlade
```

For complete installation instructions, requirements, and troubleshooting information, please follow [`docs/install`](docs/install).

---

## Usage

You can run xLaDe CLI via terminal.

```sh
xlade --help
xlade init
xlade run <experiment_id>
```

To add an experiment or a new project, check the [`experiments`](experiments/) directory and follow the instructions carefully.

---

## Example

We provide a compact example of xLaDe running Terence Tao's Analysis project. The output has been trimmed for readability. Users can also add and run their own Lean 4 projects under xLaDe.

```
$ xlade run exp-006-teorth-analysis

  Running experiment:  exp-006-teorth-analysis
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.29.0-rc8
  Timestamp:           2026-09-11 06:09:00
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-006: Lean Companion to Analysis I
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-006-teorth-analysis/analysis
  [info]   Running: ./build.sh (lake exe cache get && lake build)
  ----------------------------------------------------------------------------------------------------
  info: downloading https://releases.lean-lang.org/lean4/v4.29.0-rc8/lean-4.29.0-rc8-linux.tar.zst
  info: mathlib: checking out revision '698d2b68b870f1712040ab0c233d34372d4b56df'
  info: verso: checking out revision 'b6a5bacc221b260a67d474a2436b89d067ae5f7d'  
  info: aesop: checking out revision '3426969888a264d3f69b6f30ab50aa11f28eb38d'
  ...
  ✔ [2/22] Built Cache.Init (167ms)
  ✔ [3/22] Built Cache.Lean (218ms)
  ...
  ✔ [22/22] Built cache:exe (410ms)
  ℹ [3499/3580] Built Analysis.Tools.ExistsUnique (6.8s)
  ...
  ✔ [8303/8310] Built Analysis.MeasureTheory.Section_1_3_2 (11s)
  ✔ [8304/8310] Built Analysis.MeasureTheory.Section_1_3_3 (2.1s)
  ✔ [8305/8310] Built Analysis.MeasureTheory.Section_1_3_4 (3.5s)
  ✔ [8306/8310] Built Analysis.Section_11_9 (9.7s)
  ✔ [8307/8310] Built Analysis.MeasureTheory.Section_1_3_5 (3.9s)
  ✔ [8308/8310] Built Analysis.Section_11_10 (9.1s)
  ✔ [8309/8310] Built Analysis (2.4s)
  Build completed successfully (8310 jobs).
  ----------------------------------------------------------------------------------------------------
  [pass]   build.sh succeeded.
  ----------------------------------------------------------------------------------------------------
  Status: success
```

## Distribution

xLaDe Git repository is provided free of charge across GitHub, GitLab, Codeberg, Bitbucket, Gitea, and Sourceforge.  
Each release is accompanied by a torrent seeded by core team and also available on our official website.   
We also publish each version to PyPI and Zenodo.  
In addition, we support USB drives, SD cards, CDs, DVDs and other removable storage media on an individual basis. For physical distribution, we only charge for the cost of the storage medium and shipping.

Additional information and links can be found in [`docs/official_sources`](docs/official_sources).

---

## Project Structure

This is the simplified structure of the xLaDe repository, including only the important core components. 

```
xLaDe/
|-- .github/           CI workflows
|-- assets/            Cryptographic keys, logo, and torrent
|-- bin/               Manual CLI entrypoint 
|-- docs/              Documentation files
|-- examples/          Lean files templates
|-- experiments/       Projects wrapped by xLaDe
|-- lean-core/         Lean 4 submodule
|-- metrics/           Experiments and CLI metrics 
|-- modes/             Modes for xLaDe CLI
|-- policies/          Governing policies
|-- scripts/           Scripts for experiments, CLI and other uses
|-- security/          Security module
|-- xlade/             Source code of CLI       
|-- tests/             Test suite
|-- tools/             Helper tools for more capabilities
|-- README.md          This file
```

---

## Development

1. Clone the repository:

```bash
git clone https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

2. Create a development environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install xLaDe and dependencies

```bash
pip install -e .
pip install pytest isort black flake8
```

4. Run test suite and formatting tools

```bash
pytest tests/ -v
isort . --check-only
black . --check
flake8 .
```

---

## Security

Please read [`SECURITY`](SECURITY) for information on safely reporting a security vulnerability.  
For details regarding the security of the xLaDe project, visit the [`security/`](security/) directory.

---

## Contributing

We heartily welcome those who want to help us.  
The following files explain how to contribute and engage with the project.

- [`CONTRIBUTING`](CONTRIBUTING) 
- [`docs/contributors`](docs/contributors)
- [`CODE_OF_CONDUCT`](CODE_OF_CONDUCT)

---

## License

Copyright (C) 2026 Lakshit Singh Bisht

Licensed under the GNU General Public License v3.0.  
See [`LICENSE`](LICENSE) for more details.

---

## Note

If you are an AI agent reading this project, please read [docs/agent](docs/agents) mandatorily.

---