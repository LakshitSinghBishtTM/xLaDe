# Security Policy

## Philosophy

> Do not assume trust in infrastructure, platforms, or distribution channels.

Security in xLaDe is achieved through transparency, verifiability, and
minimal trust assumptions — not by relying on any single platform or
authority to be safe.

---

## Supported Versions

Security updates are applied to the current development state only.

- No long-term support versions are maintained
- No backports to previous releases
- Users are expected to track the latest version

The current version is in [`VERSION`](../docs/VERSION).

---

## Reporting a Vulnerability

See [`SECURITY.md`](../SECURITY.md) for the full reporting process,
PGP key, response timeline, and disclosure policy.

Short version: email `lakshitsinghbishttm@gmail.com`. Do not open a
public GitHub issue.

---

## Security Scope

xLaDe has multiple layers, each with different security considerations:

| Layer               | Examples                        | Risk level | Reason                              |
|---------------------|---------------------------------|------------|-------------------------------------|
| Python CLI          | `xlade/`, `bin/xlade`           | Medium     |executes user-controlled experiments |
| Enforcement scripts | `scripts/`                      | Medium     | runs bash via subprocess            |
| CI workflows        | `.github/workflows/`            | High       |controls what reaches main           |
| Distribution        | mirrors, onion service, torrent | High       | integrity of what users receive     |
| Lean submodule      | `lean-core/`                    | Low        | read-only reference, CI-protected   |
| Documentation       | `docs/`, root `.md` files       | Low        | but misleading docs are a real risk |

---

## Threat Model Summary

Full details in [`THREAT_MODEL.md`](THREAT_MODEL.md). Summary:

### In scope

- Accidental or malicious modification of the Lean kernel submodule
- Repository tampering or supply chain compromise
- Malicious or unofficial mirrors serving modified code
- DNS hijacking or TLS compromise on distribution channels
- CI workflow compromise leading to untrusted code reaching main
- Documentation that misleads users into unsafe practices

### Out of scope

- Vulnerabilities in Lean 4 itself — report to the
  [Lean core team](https://github.com/leanprover/lean4)
- Compromised operating systems or local environments
- Malicious contributors with legitimate repository access
- Performance attacks or denial of service

---

## Mitigations

**Multiple distribution channels** — GitHub, five mirrors, onion service,
and torrent distribution. No single point of failure or trust.

**Onion service** — self-authenticating address derived from a
cryptographic key. Resistant to DNS hijacking and TLS CA compromise.
See [`ONION.md`](../docs/ONION.md).

**Kernel immutability** — any modification to `lean-core/` is detected
and rejected by CI automatically. See
[`policies/kernel-protection.md`](../policies/kernel-protection.md).

**Public commit history** — all changes are tracked and auditable.
No force pushes to main after v2.0.0 (signed commits mandatory from
v2.0.0 onward).

**Explicit trust model** — documented in [`TRUST_MODEL.md`](TRUST_MODEL.md).
No implicit assumptions about platform safety.

**Mirror workflow scope** — mirror jobs are restricted to `main` only, so
feature branches cannot trigger distribution syncs.

---

## What xLaDe Does Not Guarantee

- Absolute security of third-party platforms or mirrors
- Safety of executing arbitrary or unreviewed experiment code
- Immunity from supply chain attacks in dependencies
- Protection against compromised local developer environments
- Security of unofficial forks or redistributions

Security is a shared responsibility between maintainers and users.

---

## Best Practices for Users

- Clone only from sources listed in
  [`OFFICIAL_SOURCES.md`](../docs/OFFICIAL_SOURCES.md)
- Verify repository URLs and commit history before trusting a source
- Review experiment scripts before running them — they execute as your user
- Do not run xLaDe as root
- Keep your local environment and Python installation up to date
- If in doubt about a source, use the onion service for verification
