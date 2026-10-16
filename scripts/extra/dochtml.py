#!/usr/bin/env python3

"""Print an HTML list of project documentation files for the website."""

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

DOC_EXTENSIONS = {".md", ".txt", ".cff"}
DOC_DIRS = {"docs", "experiments", "projects", "policies", "security"}
DOC_NAMES = {
    "readme",
    "changelog",
    "contributing",
    "contributors",
    "code_of_conduct",
    "citation",
    "license",
    "security",
}
IGNORED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", "venv",
}
def load_ignore_rules(root: Path):
    rules = []
    for gitignore in root.rglob(".gitignore"):
        directory = gitignore.parent.relative_to(root)
        if any(part in IGNORED_DIRS for part in directory.parts):
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
        candidates = ("/".join(parts[:i + 1]) for i in range(len(parts)))
        for i, candidate in enumerate(candidates):
            if (fnmatch.fnmatchcase(candidate, pattern) if anchored or "/" in pattern else fnmatch.fnmatchcase(parts[i], pattern)):
                ignored = not negated
    return ignored


def is_document(path: Path, relative_path: Path, ignore_rules, submodule_paths) -> bool:
    if any(part in IGNORED_DIRS or part.endswith(".egg-info") for part in relative_path.parts):
        return False
    if is_gitignored(relative_path, ignore_rules):
        return False
    if any(relative_path == submodule or submodule in relative_path.parents for submodule in submodule_paths):
        return False

    experiment_parts = [part for part in relative_path.parts if part.lower().startswith("exp-")]
    if experiment_parts and path.stem.casefold() != "readme":
        return False

    if path.name.casefold() == "metrics.md":
        return False

    suffix = path.suffix.lower()
    if suffix in DOC_EXTENSIONS:
        return True

    if not suffix:
        if relative_path.parts[0].lower() in DOC_DIRS:
            return True
        if path.name.lower() in DOC_NAMES:
            return True

    return False


def main() -> None:
    ignore_rules = load_ignore_rules(CODE_ROOT)
    submodule_paths = load_submodule_paths(REPO_ROOT)
    documents = sorted(
        (
            path
            for path in CODE_ROOT.rglob("*")
            if path.is_file() and is_document(path, path.relative_to(CODE_ROOT), ignore_rules, submodule_paths)
        ),
        key=lambda path: (
            (path.relative_to(CODE_ROOT).as_posix() if path.stem.casefold() == "readme" else path.name).casefold(),
            path.relative_to(CODE_ROOT).as_posix().casefold(),
        ),
    )

    previous_letter = None
    for path in documents:
        relative_path = path.relative_to(CODE_ROOT)
        display_name = path.name
        if path.stem.casefold() == "readme":
            display_name = relative_path.as_posix()
        letter = display_name[0].upper()
        if letter != previous_letter:
            print(f"<h3>{html.escape(letter)}</h3>")
            print()
            previous_letter = letter

        href = f"{WEB_PREFIX}/{quote(relative_path.as_posix(), safe='/')}"
        print("<li>")
        print(f'    <a href="{href}">{html.escape(display_name)}</a>')
        print("</li>")
        print()


if __name__ == "__main__":
    main()
