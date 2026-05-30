# Security

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Security reports should be sent privately by email:

**Email:** lakshitsinghbishttm@gmail.com

PGP-encrypted communication is strongly preferred for anything sensitive.

**PGP Public Key:**
http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion/pgp.asc
https://github.com/LakshitSinghBishtTM/xLaDe/assets/keys/pgp.asc

If you cannot access the onion site, you may request the public key by
email before sending your report.

---

## What to Include

A useful security report includes:

- A clear description of the vulnerability
- The affected version (see [`VERSION`](../VERSION))
- Steps to reproduce, if applicable
- Your assessment of severity and impact
- A patch or suggested fix, if you have one

You do not need to have all of this to report. An incomplete report is
better than no report.

---

## Response Timeline

| Stage              | Target                  |
|--------------------|-------------------------|
| Acknowledgement    | Within 3 business days  |
| Initial assessment | Within 7 business days  |
| Resolution plan    | Within 14 business days |

xLaDe is maintained by volunteers. These are targets, not guarantees.
Every report is read and taken seriously regardless of response time.

---

## Scope

Security reports are welcome for:

- The xLaDe Python CLI (`xlade/`)
- CI workflows and enforcement scripts (`scripts/`, `.github/workflows/`)
- Distribution infrastructure (mirrors, onion service)
- Documentation that could mislead users into unsafe practices

Out of scope:

- Vulnerabilities in Lean 4 itself — report those to the
  [Lean core team](https://github.com/leanprover/lean4)
- Vulnerabilities in third-party mirrors not listed in
  [`OFFICIAL_SOURCES.md`](../OFFICIAL_SOURCES.md)
- Theoretical attacks with no practical exploitation path

---

## Disclosure Policy

xLaDe follows **coordinated disclosure**:

1. You report privately
2. We acknowledge and investigate
3. We develop and test a fix
4. We release the fix and credit you (unless you prefer to remain anonymous)
5. Full details are disclosed after the fix is available

We ask for a reasonable window to address issues before public disclosure.
If we cannot agree on a timeline, you are free to disclose at your
discretion.

---

## Acknowledgements

Contributors who responsibly disclose security issues will be credited
in the release notes for the fixing version, unless they prefer otherwise.

---

## Further Reading

- [`SECURITY_POLICY.md`](docs/SECURITY_POLICY.md) — security philosophy and threat model overview
- [`THREAT_MODEL.md`](docs/THREAT_MODEL.md) — what xLaDe does and does not protect against
- [`TRUST_MODEL.md`](docs/TRUST_MODEL.md) — distribution trust model
- [`OFFICIAL_SOURCES.md`](OFFICIAL_SOURCES.md) — authoritative sources and verification