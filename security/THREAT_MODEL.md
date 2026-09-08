# Threat Model

This document explains the threat model of xLaDe project.
We are honest about the scope and not want to make it a security theatre.
We do not say xLaDe is perfectly secured and provide no absolute claims.

---

## Security Goals

We protect the following assets:

- Official Website
- Mirrors and distribution
- Release artifacts
- Signature identity
- Repository Codebase 
- Documentation
- Lean Core kernel integrity

---

## In-Scope Threats

- DNS Compromise
- TLS Compromise
- Semantic divergence
- Misleading documentation
- Repository Tampering
- Mirrors Tampering 

---

### In-scope Rationale

- The official website is an onion service. It is decentralised. We don't depend on any centralised infrastructure for hosting our website.
- The onion service has a private key and a public key which self verifies the domain. The website certifies itself, making it free from TLS compromise.
- The semantic divergence is not permissible under xLaDe and we provide authoritative documentation in case of ambiguity.  
- Documentation is a core part of xLaDe. We provide reliability and correctness to the official documentation.
- We sign commits with SSH key, whose public key is provided in assets. This provides trust for committer identity.
- Mirrors are also signed with the SSH keys in Gitlab, Codeberg, and Gitea. Sourceforge doesn't provide signing feature, so it can't be provided there.

---

## Out-of-Scope Threats

- Nation-state
- Supply chain 
- Zero-day
- Compromised OS
- Bash or terminal access
- Lean 4 attacks
- Network attacks

---

### Out-of-scope Rationale

- We don't protect against nation-state, supply chain attacks, zero-day exploits and OS compromised with malwares, trojans, etc.
- We also don't protect in case of an attacker having terminal or network access.
- xLaDe is a local CLI tool, and no internet is required to run it.
- Only the dependencies like lean, lake, mathlib, etc. require internet, so we don't provide safety from network attacks.
- Since running experiments may invoke bash, so we consider it out of scope to restrict bash. 
- However, users can always read the file before running it. The user bears the accountability of running any script.
- We don't look after protection of Lean 4. In case of any problem in Lean 4, the xLaDe team is not responsible 

---

## Trust Assumptions

- Lean 4 is trusted
- Git, Python, etc. are uncompromised
- User runs xLaDe without sudo
- CI secrets are uncompromised

In case of any trust assumption is broken, no assurance can be given.

---
