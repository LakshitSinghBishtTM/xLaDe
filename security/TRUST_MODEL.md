# Trust Model

## Overview

xLaDe is designed under a minimal-trust model, with trust explicitly divided across two domains:

1. Distribution Trust: how users obtain the project
2. Project Trust: what components are trusted within the system

This separation allows xLaDe to reduce reliance on any single platform while maintaining strong guarantees around proof correctness.

---

## 1. Distribution Trust

xLaDe is distributed across multiple independent sources:

* GitHub (primary repository)
* GitLab (mirror)
* Onion service (network-independent access)

### Assumptions

* Any single platform may be unavailable, restricted, or compromised
* DNS and TLS infrastructure may not be fully trustworthy
* Mirrors may lag or be incomplete

### Trust Strategy

* No single source is treated as authoritative in isolation
* Users are expected to verify:

  * repository URLs
  * commit history
  * version consistency

The onion service provides a self-authenticating access path, reducing reliance on traditional web trust infrastructure.

### Goal

Reduce dependency on centralized infrastructure and ensure continued accessibility under varying network conditions.

---

## 2. Project Trust

We explain the threat model considered in the design of xLaDe and discuss security considerations relevant to its experimental nature. The objective is to clearly state assumptions, trust boundaries, and potential risks associated with ecosystem-level experimentation.

### 2.1 Threat Model

The threat model for xLaDe is defined with respect to its intended use as a local, experimental framework.

The primary assets of interest are:

* Integrity of the Lean~4 proof kernel
* Correctness of proof verification

#### Trusted Components

* Lean4 kernel
* Lean compiler and core toolchain

These components are assumed to be correct and not adversarially modified.

#### Out of Scope

* Malicious kernel or compiler modification
* Compromised operating system
* Network-based or remote adversaries
* Execution in hostile environments

Instead, the model focuses on:

* unintended effects from experimental tooling
* repository structure and workflow changes
* configuration and policy behavior

---

### 2.2 Security Considerations

Given the defined threat model, xLaDe incorporates the following design choices:

#### Isolation of Experimental Components

* Tooling scripts, CLI layers, and configurations are treated as **untrusted**
* These components are isolated from the Lean kernel
* This prevents compromise of proof soundness

#### Reproducibility and Auditability

* All changes are tracked via version control
* Repository state is reproducible
* Experiments are explicit and reversible

This enables:

* tracing the origin of changes
* rollback of unsafe modifications

#### Transparency

* Clear distinction between trusted and experimental layers
* Documented assumptions and limitations

This reduces the risk of misuse or misinterpretation.

---

## Relationship to Other Documents

* `OFFICIAL_SOURCES.md`: defines where to obtain the project
* `MIRRORS.md`: describes replication strategy
* `ONION.md`: defines alternative access model
* `SECURITY.md`: vulnerability reporting process
* `SECURITY_POLICY.md`: broader security philosophy