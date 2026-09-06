# Trust Model

This document defines what xLaDe trusts, what it does not trust, and
how that shapes the project's design and distribution strategy.

---

## Two Domains of Trust

xLaDe separates trust into two distinct domains:

1. **Distribution trust** — how users obtain the project
2. **Component trust** — what is trusted within the running system

---

## 1. Distribution Trust

### The Problem

Any single distribution channel can be compromised, restricted, or
made unavailable. GitHub can go down. DNS can be hijacked. A TLS
certificate authority can be compromised. A mirror can serve stale
or modified content.

A project that depends entirely on GitHub for distribution is one
platform outage or account compromise away from being inaccessible.

### xLaDe's Approach

xLaDe distributes across multiple independent channels:

| Channel                                          | Trust properties                                           |
|--------------------------------------------------|------------------------------------------------------------|
| GitHub (primary)                                 | Convenient, widely trusted, single point of failure        |
| GitLab, Codeberg, Bitbucket, Gitea, SourceForge  | Independent mirrors, reduce single-platform dependency     |
| Onion service                                    | Self-authenticating, censorship-resistant, DNS-independent |
| Torrent                                          | Decentralised, no central server required                  |

No single source is treated as authoritative in isolation. Users are
expected to verify what they receive.

### The Onion Service

The onion service address is derived from a cryptographic key. This
means the address itself is a form of identity — a server at that
address controls the corresponding private key. Unlike a domain name,
it cannot be hijacked via DNS or spoofed via a rogue certificate
authority.

This is why the onion service is the **official project website**,
not a fallback. It provides stronger identity guarantees than any
clearnet hostname.

### User Responsibilities

- Clone only from sources listed in
  [`OFFICIAL_SOURCES.md`](../docs/OFFICIAL_SOURCES.md)
- Verify repository URLs before trusting them
- Cross-check commit history between sources if integrity is critical
- Do not trust mirrors or forks not listed in official sources

---

## 2. Component Trust

### Trusted Components

These components are assumed to be correct and are not modified by
xLaDe under any circumstances:

| Component                   | Why trusted                                 |
|-----------------------------|---------------------------------------------|
| Lean 4 kernel               | Upstream, immutable submodule, CI-protected |
| Lean compiler and toolchain | Installed via elan from official sources    |

The Lean kernel is the foundation everything else depends on. If the
kernel is compromised, no ecosystem-layer tool can compensate. xLaDe's
only defence here is to never touch it — which is enforced by CI.

### Untrusted Components

These components are treated as potentially unsafe and isolated from
the trusted core:

| Component                        | Why untrusted                           |
|----------------------------------|-----------------------------------------|
| Python CLI (`xlade/`)            | Application code, not formally verified |
| Enforcement scripts (`scripts/`) | Bash scripts executed via subprocess    |
| Experiment code                  | User-contributed, runs as current user  |
| CI workflows                     | Could be modified by a PR               |
| Configuration files              | User-controlled                         |

Treating these as untrusted means:

- They are isolated from the Lean kernel by design
- They cannot modify `lean-core/` (enforced by CI)
- Their effects are explicit, documented, and reversible
- A bug or malicious modification here cannot compromise proof soundness

### The Isolation Guarantee

The separation between trusted (Lean kernel) and untrusted (everything
else) is not just documented — it is enforced. CI rejects any PR that
modifies `lean-core/`. This means the integrity of the kernel does not
depend on contributor good faith — it depends on CI, which is itself
auditable.

---

## What This Model Does Not Cover

- **Malicious maintainers** — a maintainer with repository access could
  modify CI to stop enforcing kernel protection. This is outside the
  scope of the trust model.
- **Compromised local environments** — if the user's machine is
  compromised, no application-level trust model applies.
- **Lean 4 itself** — the trust model assumes the Lean kernel is correct.
  It does not verify this.

---

## Relationship to Other Documents

- [`SECURITY.md`](../SECURITY.md) — vulnerability reporting
- [`SECURITY_POLICY.md`](SECURITY_POLICY.md) — security philosophy and mitigations
- [`THREAT_MODEL.md`](THREAT_MODEL.md) — specific threats and defences
- [`../docs/OFFICIAL_SOURCES.md`](../docs/OFFICIAL_SOURCES.md) — authoritative distribution sources
- [`../docs/ONION.md`](../docs/ONION.md) — onion service rationale
- [`../docs/MIRRORS.md`](../docs/MIRRORS.md) — mirror list and consistency expectations