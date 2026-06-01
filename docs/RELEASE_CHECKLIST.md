# Release Checklist

## NOTE: This file is only for the Core Team and Maintainers of project!
## Not to be read by or useful for others 

This document lists every file that needs updating before tagging a new release.
Work through it top to bottom. Do not tag until all steps are done.

---

## 1. Version Bump - Update These Files

Every release requires updating the version string in all of these:

| File                 | What to change                                     |
|----------------------|----------------------------------------------------|
| `VERSION`            | The version string itself                          |
| `pyproject.toml`     | `version = "x.y.z"` under `[project]`              |
| `xlade/cli/main.py`  | `VERSION = "x.y.z"` at the top                     |
| `README.md`          | Badge: `version-x.y.z-blue`                        |
| `lake-manifest.json` | `"version": "x.y.z"`                               |
| `CITATION.cff`       | `version: "x.y.z"` and `date-released:`            |

---

## 2. Release Notes - Write These

| File           | What to add                                             |
|----------------|---------------------------------------------------------|
| `CHANGELOG.md` | New version section - highlights, added, changed, notes |
| `RELEASES.md`  | New version entry mirroring CHANGELOG highlights        |
| `README.md`    | As of version x.y.z at the end of the README.md         |

---

## 3. Distribution - Update If Needed

| File           | What to change                                             |
|----------------|------------------------------------------------------------|
| `README.md`    | Torrent link and magnet URL - point to new version tarball |
| `CITATION.cff` | DOI for publishing a new Zenodo record for this release    |

---

## 4. Final Checks Before Tagging

```sh
# confirm version is consistent
cat VERSION
grep 'version' pyproject.toml
grep 'VERSION' xlade/cli/main.py
grep 'version-' README.md

# run tests one last time
pytest tests/ -v

# confirm all changes are staged
git status
```

All tests must pass. `git status` should show nothing untracked or unstaged.

---

## 5. Commit, Tag, Push

```sh
git add -A
git commit -m "release v<version>"
git push origin main
# wait for CI to pass on GitHub before tagging

git tag v<version>
git push origin v<version>
```

Pushing the tag triggers `cd.yml` which runs the test suite, builds the
Python package, and creates the GitHub Release automatically.

---

## 6. After Release

- Verify the GitHub Release was created at: `https://github.com/LakshitSinghBishtTM/xLaDe/releases`
- Verify mirrors sync (check GitLab, Codeberg, Bitbucket, and Gitea)
- Update the SourceForge mirror manually
- Update the Zenodo record
- Update the torrent file in `assets/torrent/` for the new version

---

## Notes

- The torrent magnet URL in `README.md` is version-specific - generate
  a new one after the GitHub Release is created and the tarball is available
- `lake-manifest.json` version should match `VERSION` for consistency
  but does not affect build behaviour
