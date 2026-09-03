# Security

At xLaDe, we take the security of the project seriously.
This document describes how to report the vulnerabilities securely to us.

---

## What Not to do

- Opening an issue in Github or other forges
- Writing an article anywhere
- Providing operational information publicly
- Using an insecure communication channel

---

## How to report

- Send a PGP-encrypted email to lakshitsinghbishttm@gmail.com

---

### PGP Public Key

We publish our PGP key in multiple places. Obtain from any of the following sources.

- http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion/pgp.asc
- https://github.com/LakshitSinghBishtTM/xLaDe/assets/keys/pgp.asc
- https://keys.openpgp.org/vks/v1/by-fingerprint/1520CEF8218F97F8A6CA4473B79C23D508EF3F92

If there is still any problem in finding the key, you can ask us for PGP key in the first email before reporting.
We will be happy to share it.

---

## What to include

Please create a document file (we normally prefer a .txt file, but any format is fine.)
In the file, please include two types of details:

### Mandatory details

- A description of the vulnerability
- Version in which it was found
- How you found it
- Any comments or details

The mandatory details depend on vulnerability's context and may be different from listed above.
Please send us as many details as possible.

### Optional details

- Affected versions
- Rigorous steps to reproduce
- Fix or patch for vulnerability

---

## Scope

We welcome reports on

- The xLaDe CLI tool
- Entire project files and codebase
- Mirrors and infrastructure of xLaDe
- xLaDe official website

Please don't report following to us

- Vulnerabilities of xLaDe dependencies such as Lean 4, Bash, Git, etc.
- Theoretical attacks with no practical exploitation path

---

## Disclosure Policy

We follow the following process

1. You report privately
2. We investigate the vulnerability
3. We develop the fix
4. We release it and credit the finder
5. DCVE is released for the issue publicly if applicable

After the vulnerability is fixed and DCVE is released, the finder is free to write article or public report on the vulnerability.

---

## Acknowledgements

We will acknowledge the finder of vulnerabilities in the DCVEs issued by xLaDe.
In addition, we will also credit in the security page of xLaDe website.
The finder can ask to remain anonymous if he/she wants.

---

## Further Reading

- [`SECURITY_POLICY.md`](security/SECURITY_POLICY.md)
- [`THREAT_MODEL.md`](security/THREAT_MODEL.md)
- [`TRUST_MODEL.md`](security/TRUST_MODEL.md)
- [`DCVES/`](security/advisories/)

---

## Note

In case of anything missing in the document, please report to us.

---
