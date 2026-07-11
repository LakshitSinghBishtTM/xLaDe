#!/usr/bin/env python3

from pathlib import Path
import html

ROOT = Path(".").resolve()
WEB_PREFIX = "files/code"

IGNORE = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    ".xlade",
}


def should_ignore(path: Path) -> bool:
    return any(part in IGNORE for part in path.parts)


def link(relpath: Path) -> str:
    href = f"{WEB_PREFIX}/{relpath.as_posix()}"
    name = html.escape(relpath.name)
    return f'<a href="{href}">{name}</a>'


def children(path: Path):
    items = [
        p for p in sorted(
            path.iterdir(),
            key=lambda x: (x.is_file(), x.name.lower())
        )
        if not should_ignore(p)
    ]
    return items


lines = []


def walk(path: Path, prefix=""):
    items = children(path)

    for i, item in enumerate(items):
        last = (i == len(items) - 1)

        branch = "`- " if last else "|- "

        if item.is_dir():
            lines.append(prefix + branch + item.name + "/")

            extension = "   " if last else "|  "
            walk(item, prefix + extension)

        else:
            rel = item.relative_to(ROOT)
            lines.append(prefix + branch + link(rel))


lines.append(ROOT.name + "/")
walk(ROOT)

print("<pre>")
print("\n".join(lines))
print("</pre>")