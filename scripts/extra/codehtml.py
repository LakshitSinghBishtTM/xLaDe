#!/usr/bin/env python3

"""Print a linked source tree for the xLaDe website."""

import fnmatch
import html
import subprocess
from pathlib import Path
from urllib.parse import quote

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
WEBSITE_CODE_ROOT = REPO_ROOT.parent.parent / "websites" / "xLaDe" / "files" / "code"
CODE_ROOT = WEBSITE_CODE_ROOT if WEBSITE_CODE_ROOT.is_dir() else REPO_ROOT
WEB_PREFIX = "files/code"

IGNORE = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    "venv",
    ".xlade",
}


def load_ignore_rules(root: Path):
    rules = []
    for gitignore in root.rglob(".gitignore"):
        directory = gitignore.parent.relative_to(root)
        if any(part in IGNORE for part in directory.parts):
            continue
        for line in gitignore.read_text(encoding="utf-8", errors="replace").splitlines():
            rule = line.strip()
            if rule and not rule.startswith("#"):
                rules.append((directory, rule))
    return rules


def load_submodule_paths(root: Path) -> set[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "-c", "core.quotepath=false", "submodule", "status"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return set()

    paths = set()
    for line in result.stdout.splitlines():
        fields = line[1:].split(maxsplit=1)
        if len(fields) == 2:
            paths.add(Path(fields[1].split(" (", maxsplit=1)[0]))
    return paths


def is_gitignored(relative_path: Path, rules) -> bool:
    ignored = False
    for directory, rule in rules:
        negated = rule.startswith("!")
        pattern = rule[1:] if negated else rule
        if not pattern:
            continue
        anchored = pattern.startswith("/")
        pattern = pattern.strip("/")
        try:
            scoped = relative_path.relative_to(directory)
        except ValueError:
            continue
        parts = scoped.parts
        for i in range(len(parts)):
            candidate = "/".join(parts[:i + 1])
            matched = (fnmatch.fnmatchcase(candidate, pattern)
                       if anchored or "/" in pattern
                       else fnmatch.fnmatchcase(parts[i], pattern))
            if matched:
                ignored = not negated
    return ignored


def should_ignore(path: Path, relative_path: Path, ignore_rules, submodule_paths) -> bool:
    return (
        path.name.endswith(".pyc")
        or any(part in IGNORE or part.endswith(".egg-info") for part in relative_path.parts)
        or is_gitignored(relative_path, ignore_rules)
        or any(relative_path == submodule or submodule in relative_path.parents for submodule in submodule_paths)
    )


def link(relpath: Path) -> str:
    href = f"{WEB_PREFIX}/{quote(relpath.as_posix(), safe='/')}"
    name = html.escape(relpath.name)
    return f'<a href="{href}">{name}</a>'


def children(path: Path, ignore_rules, submodule_paths):
    items = [p for p in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
             if not should_ignore(p, p.relative_to(CODE_ROOT), ignore_rules, submodule_paths)]
    return items


def walk(path: Path, ignore_rules, submodule_paths, lines, prefix=""):
    items = children(path, ignore_rules, submodule_paths)

    for i, item in enumerate(items):
        last = i == len(items) - 1

        branch = "`- " if last else "|- "

        if item.is_dir():
            lines.append(prefix + branch + item.name + "/")

            extension = "   " if last else "|  "
            walk(item, ignore_rules, submodule_paths, lines, prefix + extension)

        else:
            rel = item.relative_to(CODE_ROOT)
            lines.append(prefix + branch + link(rel))


def main() -> None:
    lines = [CODE_ROOT.name + "/"]
    walk(CODE_ROOT, load_ignore_rules(CODE_ROOT), load_submodule_paths(REPO_ROOT), lines)

    print("<pre>")
    print("\n".join(lines))
    print("</pre>")


if __name__ == "__main__":
    main()
