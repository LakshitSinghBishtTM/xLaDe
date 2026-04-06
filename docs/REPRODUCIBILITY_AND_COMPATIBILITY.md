# Reproducibility and Compatibility in xLaDe

## Background

Lean is designed for rapid evolution. As noted by its developers,
the system prioritizes scalability and correctness over long-term
backward compatibility. As a result, Lean code written in earlier
versions may not compile unchanged in later versions.

## Problem

This creates challenges for:

- long-term reproducibility of experiments
- comparison of results across Lean versions
- preservation of ecosystem-level research artifacts
- onboarding users working with older materials

In traditional workflows, these issues are handled manually, often requiring ad-hoc fixes or migration effort.

## xLaDe Approach

xLaDe does not attempt to modify Lean or enforce backward compatibility.

Instead, xLaDe introduces a different model:

> Experiments are defined by both their code and their environment.

Each experiment can specify:

- the Lean toolchain version
- dependencies and build configuration
- execution context (mode, policies)

xLaDe records and exposes this information, enabling:

- reproducibility of experiments under their original environment
- explicit detection of environment mismatches
- comparison across different execution contexts

## Current Implementation

As of now, xLaDe provides:

- environment metadata via `experiment.toml`
- tracking of experiment execution in `.xlade/metrics.json`
- display of required Lean toolchain during execution
- mode-aware experiment control

## Future Plan

Future work will include:

- Automation of environment setup via script
- experiment-scoped toolchain switching
- tracking experiment behavior across Lean versions
- tooling for detecting and analyzing breakages
- comparative analysis across environments


## Summary

In xLaDe, we are trying to shift the focus from backward compatibility to reproducibility. As a result, this major problem of Lean 4 can be controlled and mitigated. Comments and feedback on this are welcomed to find better solutions!