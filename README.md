<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/xlade-logo-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/logo/xlade-logo-light.png">
    <img alt="xLaDe Logo" src="assets/logo/xlade-logo.svg" width="260">
  </picture>
</p>

<h2 align="center">xLaDe</h2>
<p align="center">eXperimental Lean 4 advanced Development ecosystem</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/version-1.6.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/status-experimental-orange" alt="Status">
  <img src="https://img.shields.io/badge/Lean-4-purple" alt="Lean 4">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20BSD%20%7C%20Android-lightgrey" alt="Platform">
  <a href="https://github.com/LakshitSinghBishtTM/xLaDe/graphs/contributors"><img src="https://img.shields.io/github/contributors/LakshitSinghBishtTM/xLaDe?color=green" alt="Contributors"></a>
  <a href="https://github.com/LakshitSinghBishtTM/xLaDe/issues"><img src="https://img.shields.io/github/issues/LakshitSinghBishtTM/xLaDe" alt="Issues"></a>
</p>

---

Lean 4 proofs break silently across versions. Projects built on Lean drift
from upstream until one day they simply stop working. Nobody knows why.
These are not edge cases. They are the normal experience of working with
a proof assistant under rapid development.

**xLaDe is a research platform that studies these problems and builds
tooling to address them.** It is not a theorem library, a fork of Lean,
or a replacement for any existing tool. It is an ecosystem layer — a
controlled environment for running experiments on how Lean is *used*,
enforcing architectural boundaries that prevent kernel drift, and recording
enough metadata to reproduce any experiment correctly, years later.

xLaDe is built primarily as a command-line tool for Linux, with tested support for Windows (via WSL) and Android (via Termux). It installs through pip, ships with a comprehensive test suite and remains experimental.

---

## The Problems

### Lean proofs are fragile over time

Lean 4 evolves fast. A proof that compiles today may fail elaboration
next year as the toolchain changes. This is acknowledged by the Lean
core team. It is a deliberate trade-off for a language under active
research development. But it makes reproducible research with Lean
genuinely difficult. Experiments become snapshots. Snapshots rot.

**xLaDe's response:** treat each experiment as inseparable from its
environment. Every experiment records its toolchain version, dependencies,
and execution context. The goal is reproducibility i.e., being able to
reconstruct the exact environment an experiment ran in, on demand,
years later rather than backward compatibility, which Lean cannot
guarantee.

### Lean projects drift from upstream and break

When a project builds directly on top of a Lean fork, it gradually
diverges. Features get patched in. Workarounds accumulate. The fork
drifts. One day something breaks and there is no clear record of what
was keeping it stable. Diagnosing this often requires understanding both
the original Lean codebase and every local modification made on top of
it. Sometimes it is simply not recoverable.

**xLaDe's response:** treat the Lean kernel as immutable infrastructure.
Lean is included as a Git submodule. Any modification to it is detected
by CI and the build fails. The boundary is enforced, not just documented.
All experimental effects are attributable to ecosystem decisions, not
kernel changes.

---

## What xLaDe Provides

```
xlade init                          Initialise a workspace
xlade mode experimental             Select a mode
xlade list experiments              Discover available experiments
xlade run exp-002-kernel-boundary   Run an experiment
xlade status                        View run summary
xlade metrics                       View full run history
xlade doctor                        Diagnose environment issues
xlade check                         Quick structural check
```

**Experiments** are the primary artifact. Each is a self-contained
directory with a declared hypothesis, enforcement mechanism, lifecycle
state, and exit criteria. They run via `xlade run`. Results are written
to `.xlade/metrics.json` on every execution - success, failure, or skip.

**Modes** control which experiments are enabled and how strictly policies
are enforced. Three modes: `experimental`, `stable`, `onboarding`.

**Doctor** diagnoses your environment and tells you exactly what to run
to fix each issue, not just what is missing.

**Metrics** give you a structured audit trail of every experiment run,
readable in the terminal or processable as JSON.

---

## Quick Start

**Requirements:** Python 3.11+, git, bash.
For Lean experiments: elan + Lake (see [`INSTALL.md`](INSTALL.md)).

```sh
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
pip install -e .
xlade doctor
xlade init
xlade mode experimental
xlade list experiments
xlade run exp-002-kernel-boundary
xlade run exp-003-doc-coverage
xlade status
```

Full installation guide including elan, Lean toolchain, and platform-specific
notes: [`INSTALL.md`](INSTALL.md).

---

## Active Experiments

| Experiment                | Type          | What it enforces                                   | Requires |
|---------------------------|---------------|----------------------------------------------------|----------|
| `exp-001-proof-review`    | lean-policy   | Proof review markers via Lake script               | Lake     |
| `exp-002-kernel-boundary` | script-policy | No modifications to `lean-core/`                   | bash     |
| `exp-003-doc-coverage`    | script-policy | README present in all experiments, modes, policies | bash     |

EXP-002 and EXP-003 run on any machine with bash. EXP-001 requires a
full Lean 4 + Lake installation via elan and skips cleanly without it.

---

## Build Modes

| Mode           | Experiments | Enforcement | For                   |
|----------------|-------------|-------------|-----------------------|
| `experimental` | Enabled     | Warnings    | Research, development |
| `stable`       | Disabled    | Strict      | Validation, review    |
| `onboarding`   | Disabled    | Minimal     | New users             |

---

## Distribution

xLaDe is distributed across multiple platforms to reduce reliance on
any single provider.

| Platform             | URL                                                                     |
|----------------------|-------------------------------------------------------------------------|
| **GitHub** (primary) | https://github.com/LakshitSinghBishtTM/xLaDe                            |
| GitLab               | https://gitlab.com/LakshitSinghBishtTM/xLaDe                            |
| Codeberg             | https://codeberg.org/lakshitsinghbishttm/xLaDe                          |
| Bitbucket            | https://bitbucket.org/lakshitsinghbishttm/xlade                         |
| Gitea                | https://gitea.com/LakshitSinghBishtTM/xLaDe                             |
| Sourceforge          | https://sourceforge.net/projects/xlade                                  |
| **Website**          | `http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion` |

The onion service is the official project website, not a mirror or
fallback. See [`ONION.md`](ONION.md) for the rationale.

**Torrent:** [`assets/torrent/xlade_v1.5.0.torrent`](assets/torrent/xlade_v1.5.0.torrent)

```
magnet:?xt=urn:btih:505e2102944e38609e7104170244e3c587e33a80&xt=urn:btmh:12201a2b492ddd2b4a9fc24c4c670b7e1e8f737b25efecfa24ed4463382d14e32ef1&dn=xlade&xl=2483089&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&ws=https://github.com/LakshitSinghBishtTM/xLaDe/archive/refs/tags/v1.5.0.tar.gz
```

---

## Documentation

| Document                                                                                 | Objective                                            |
|------------------------------------------------------------------------------------------|------------------------------------------------------|
| [`INSTALL.md`](INSTALL.md)                                                               | Installation - elan, Lean, pip, all platforms        |
| [`docs/WHY_xLaDe.md`](docs/WHY_xLaDe.md)                                                 | The problems in detail and why this approach         |
| [`docs/CLI_DEMO.md`](docs/CLI_DEMO.md)                                                   | Every command, with real expected output             |
| [`docs/END_TO_END_TRACE.md`](docs/END_TO_END_TRACE.md)                                   | Full session trace from clone to results             |
| [`docs/architecture.md`](docs/architecture.md)                                           | Component boundaries, directory structure, CLI layer |
| [`docs/RESEARCH_SCOPE.md`](docs/RESEARCH_SCOPE.md)                                       | Scope, non-goals, what is permanently out of scope   |
| [`docs/roadmap.md`](docs/roadmap.md)                                                     | Engineering roadmap from v1.5.0 to v2.0.0            |
| [`docs/research_roadmap.md`](docs/research_roadmap.md)                                   | Long-term research directions                        |
| [`docs/REPRODUCIBILITY_AND_COMPATIBILITY.md`](docs/REPRODUCIBILITY_AND_COMPATIBILITY.md) | Reproducibility model and staged plan                |
| [`LIMITATIONS.md`](LIMITATIONS.md)                                                       | Honest current limitations                           |
| [`CHANGELOG.md`](CHANGELOG.md)                                                           | Full version history                                 |
| [`HOW_TO_READ_THIS_REPO.md`](HOW_TO_READ_THIS_REPO.md)                                   | Where to start for new contributors                  |

---

## Repository Structure

```
xLaDe/
├── .github/           CI - tests, kernel protection, mirrors
├── experiments/       Ecosystem experiments (directory name = experiment ID)
├── xlade/             Python CLI package
│   ├── cli/           
│   └── core/          
├── scripts/           Policy enforcement shell scripts
├── modes/             Mode definitions (experimental / stable / onboarding)
├── policies/          Governance documents
├── metrics/           Research artifact files
├── security/          Threat model, trust model, security policy
├── tests/             Comprehensive test suite
├── lean-core/         Lean 4 submodule (immutable)
├── docs/              All documentation
├── pyproject.toml     Python packaging
├── lean-toolchain     Pinned Lean compiler version
└── VERSION            Current version
```

---

## Security

xLaDe operates under a minimal-trust model. No single platform is
treated as inherently trustworthy.

- [`security/SECURITY.md`](security/SECURITY.md) - how to report vulnerabilities
- [`security/THREAT_MODEL.md`](security/THREAT_MODEL.md) - what is and is not in scope
- [`security/TRUST_MODEL.md`](security/TRUST_MODEL.md) - distribution trust model
- [`security/SECURITY_POLICY.md`](security/SECURITY_POLICY.md) - security philosophy

---

## Contributing

Contributions are welcome - experiments, documentation, tooling, tests,
and feedback at any stage of development.

- [`CONTRIBUTING.md`](CONTRIBUTING.md) - how to contribute
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) - community standards
- [`CONTRIBUTORS.md`](CONTRIBUTORS.md) - acknowledgements

Contributions that modify the Lean kernel are not accepted.
This is not a policy that will change.

---

## Status

xLaDe is experimental. It is a research tool, not production software.
No stability guarantees, no backward compatibility guarantees, no support SLA.

As of `v1.6.0`:

- CLI tool improved massively
- CI and CD added and integrated
- A comprehensive suite with 83 tests

---

## License

Copyright (C) 2026 Lakshit Singh Bisht

Licensed under the **GNU General Public License v3.0**.
See [`LICENSE`](LICENSE) for full terms.

This project depends on Lean 4, licensed under the Apache License 2.0,
included unmodified as a Git submodule.

---

## Developer Note

Thank you for taking the time to read this documentation.

xLaDe is still experimental and continues to evolve with every release.
If you have ideas, feedback, criticisms, or would like to contribute,
we would be happy to hear from you.

Every contribution, suggestion, bug report, and discussion helps make
the project better.
