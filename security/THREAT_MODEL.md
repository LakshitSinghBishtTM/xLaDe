# Threat Model

This document defines what xLaDe does and does not attempt to protect
against. It is written to be honest about scope rather than to appear
more secure than the project actually is.

---

## Primary Assets

The things xLaDe is designed to protect:

| Asset                        | Why it matters                                                                       |
|------------------------------|--------------------------------------------------------------------------------------|
| Lean kernel integrity        | Experiments must not modify the trusted proof kernel                                 |
| Semantic stability           | Experimental effects must be attributable to ecosystem decisions, not kernel changes |
| Reproducibility              | An experiment run today must be reproducible in the future                           |
| Distribution integrity       | Users must receive code that matches what was committed                              |
| Documented trust boundaries  | Misleading security documentation is itself a risk                                   |

---

## In-Scope Threats

These are threats xLaDe actively defends against:

**Accidental kernel modification**
A contributor modifies `lean-core/` unintentionally — through a merge,
a rebase gone wrong, or misunderstanding the repository structure. CI
detects this and fails the build. No PR touching `lean-core/` can be
merged.

**Silent semantic divergence**
Experimental tooling changes Lean behaviour without the change being
visible or documented. The submodule model prevents this — `lean-core/`
is read-only and pinned to a specific commit.

**Repository tampering**
An attacker modifies repository content on a mirror or compromised
platform. Mitigated by multiple independent distribution channels and
the onion service's self-authenticating address.

**DNS and TLS compromise**
An attacker intercepts traffic to GitHub or mirrors via DNS hijacking
or a rogue certificate authority. The onion service is resistant to
both — its address is derived from a cryptographic key, not DNS.

**Unreviewed workflow changes**
A PR modifies CI workflows in a way that allows untrusted code to reach
main. Addressed through code review requirements and, from v2.0.0,
mandatory signed commits.

**Irreversible experiments**
An experiment modifies state in a way that cannot be undone without
manual intervention. All xLaDe experiments are designed to be reversible
— deleting `.xlade/` resets project state completely.

**Misleading documentation**
Documentation that leads users to trust unofficial sources, skip
verification, or misunderstand the security model. Addressed by
maintaining explicit `OFFICIAL_SOURCES.md` and `TRUST_MODEL.md`.

---

## Out-of-Scope Threats

These are explicitly not addressed by xLaDe:

**Malicious contributors with legitimate access**
A maintainer or contributor with repository access intentionally
introduces malicious code. xLaDe does not defend against this. Users
should apply their own judgment about trusting the project.

**Compromised operating system or local environment**
If the machine running xLaDe is compromised, xLaDe provides no
protection. This is outside the scope of any application-level tool.

**Vulnerabilities in Lean 4 itself**
Bugs or security issues in the Lean compiler, elaborator, or kernel are
out of scope. Report those to the
[Lean core team](https://github.com/leanprover/lean4).

**Supply chain attacks on dependencies**
xLaDe has minimal Python dependencies (setuptools, tomllib from stdlib).
No active monitoring of dependency vulnerabilities is performed. Users
should apply standard Python supply chain hygiene.

**Performance attacks or resource exhaustion**
No rate limiting, sandboxing, or resource controls are applied to
experiment execution.

**Network-based or remote adversaries**
xLaDe is a local CLI tool. It makes no network requests during normal
operation. The threat model does not consider network-based attacks
against the running tool.

---

## Trust Assumptions

The following are assumed to be true for the threat model to hold:

- The Lean 4 kernel and compiler are correct and unmodified
- CI enforcement is authoritative — a passing CI build means the
  kernel boundary check and test suite both passed
- Contributors follow the documented processes in good faith
- The user's local Python installation is not compromised
- The user cloned from an official source listed in
  [`OFFICIAL_SOURCES.md`](../OFFICIAL_SOURCES.md)

If any of these assumptions are violated, the threat model does not
apply and no security guarantees can be made.

---

## Residual Risks

Risks that are in scope but only partially mitigated:

- **Mirror lag** — mirrors may serve an older version. Users should
  verify version consistency against the primary repository.
- **Experiment script execution** — script-policy experiments run bash
  scripts as the current user. A malicious experiment could cause harm.
  Users should review experiment scripts before running them.
- **Unsigned commits before v2.0.0** — commit authorship cannot be
  cryptographically verified until v2.0.0 introduces mandatory GPG
  signing.

---

## Relationship to Other Documents

- [`SECURITY.md`](SECURITY.md) — how to report vulnerabilities
- [`SECURITY_POLICY.md`](SECURITY_POLICY.md) — security philosophy and mitigations
- [`TRUST_MODEL.md`](TRUST_MODEL.md) — distribution and project trust model
- [`../policies/kernel-protection.md`](../policies/kernel-protection.md) — kernel immutability enforcement
- [`../OFFICIAL_SOURCES.md`](../OFFICIAL_SOURCES.md) — authoritative sources