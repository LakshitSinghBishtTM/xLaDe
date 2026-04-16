# Mirrors

## Overview

xLaDe maintains mirrors to improve availability and reduce reliance on a single hosting platform.

Mirrors are part of the project's distribution strategy, but they are **not authoritative sources**.

---

## Current Mirrors

### GitLab

* https://gitlab.com/LakshitSinghBishtTM/xLaDe

### Codeburg

* https://codeberg.org/lakshitsinghbishttm/xLaDe

### Bitbucket

* https://bitbucket.org/lakshitsinghbishttm/xlade

### Gitea

* https://gitea.com/LakshitSinghBishtTM/xLaDe

### Sourceforge

* https://sourceforge.net/projects/xlade/


---

## Purpose of Mirrors

Mirrors exist to:

* Provide redundancy in case of platform outages
* Improve accessibility in restricted environments
* Support long-term availability of the project

---

## Trust Model

Mirrors are **not treated as sources of truth**.

The canonical repository is defined in `OFFICIAL_SOURCES.md`.

Users should:

* Prefer the primary repository for contributions
* Use mirrors for access when the primary source is unavailable
* Verify consistency between mirrors and the primary repository

---

## Consistency Expectations

* Mirrors may lag behind the primary repository
* Temporary inconsistencies may occur
* Not all metadata (issues, pull requests) may be mirrored

---

## Security Considerations

Mirrors may be:

* Incomplete
* Outdated
* Unofficially replicated by third parties

Users should verify:

* Repository origin
* Commit history
* Version consistency

Do not assume a mirror is trustworthy unless it is listed in `OFFICIAL_SOURCES.md`.

---

## Adding New Mirrors

New mirrors may be added in the future to improve resilience.

Any official mirror will be:

* Listed in `OFFICIAL_SOURCES.md`
* Announced through the primary repository

---

## Relationship to Other Documents

* `OFFICIAL_SOURCES.md`: defines authoritative sources
* `ONION.md`: describes the official website
* `SECURITY_POLICY.md`: broader security considerations