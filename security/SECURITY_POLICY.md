# Security Policy

## Overview

Security in this project is approached with a simple principle:

> Do not assume trust in infrastructure, platforms, or distribution channels.

Instead, this project emphasizes:

* Transparency
* Verifiability
* Minimal trust assumptions

---

## Supported Versions

Security updates are applied to the current development state of the repository.

At this stage of the project:

* No long-term support (LTS) versions are maintained
* Users are expected to track the latest version

---

## Reporting a Vulnerability

Please refer to `docs/SECURITY.md`

---

## Security Scope

This project includes multiple layers:

* Lean-based core logic
* Python CLI tooling
* Experiment and policy framework
* Distribution infrastructure (mirrors, onion service)

Security considerations apply across all layers.

---

## Threat Model

This project explicitly considers the following risks:

### Infrastructure Risks

* Platform compromise (e.g., Git hosting services)
* DNS manipulation or hijacking
* TLS certificate authority compromise

### Distribution Risks

* Malicious or unofficial mirrors
* Repository tampering
* Incomplete or inconsistent replication

### Supply Chain Risks

* Vulnerable or malicious dependencies
* Toolchain compromise
* Build process manipulation

### Local Risks

* Compromised developer environments
* Unsafe execution of untrusted code

---

## Mitigations

The project adopts the following strategies:

### Multiple Distribution Channels

* Primary repository + mirrors
* Onion service for independent access

### Transparency

* Public commit history
* Open development process

### Verifiability

* Users are encouraged to:

  * Inspect code before execution
  * Verify repository sources
  * Cross-check mirrors

### Minimal Assumptions

* No single platform is treated as inherently trustworthy
* Users are expected to apply independent verification where appropriate

---

## What This Project Does NOT Guarantee

* Absolute security of third-party platforms
* Safety of executing arbitrary or unreviewed code
* Immunity from supply chain attacks
* Protection against compromised local environments

Security is a shared responsibility between maintainers and users.

---

## Onion Service Considerations

An official onion service is provided (see `ONION.md`).

It helps mitigate:

* DNS and TLS-based attacks
* Certain forms of censorship

However, it does not replace the need for:

* Code review
* Source verification

---

## Best Practices for Users

Users are encouraged to:

* Clone repositories only from official sources
* Verify repository URLs and commit history
* Review code before running it
* Avoid blindly trusting mirrors or forks
* Keep their local environment secure

---

## Philosophy

Security is not achieved by trusting platforms.

Security is achieved by:

* Reducing assumptions
* Increasing transparency
* Enabling verification

This project is designed with that philosophy in mind.
