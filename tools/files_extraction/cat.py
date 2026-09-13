"""Display and inspect Lean files from the xLaDe command line."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

DECLARATION_PATTERN = re.compile(
    r"^\s*(theorem|lemma|def|abbrev|structure|inductive|class|instance|example|opaque|axiom|namespace|section)\s+"
    r"([^\s(:=]+)"
)
IMPORT_PATTERN = re.compile(r"^\s*import\s+(.+?)\s*$")


def parse_line_range(value: str) -> tuple[int, int]:
    """Parse a one-based inclusive line range such as `10-25`."""
    try:
        start_text, end_text = value.split("-", 1)
        start, end = int(start_text), int(end_text)
    except ValueError as error:
        raise argparse.ArgumentTypeError("line range must look like START-END") from error
    if start < 1 or end < start:
        raise argparse.ArgumentTypeError("line range must start at 1 and end after START")
    return start, end


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for `xlade cat`."""
    parser = argparse.ArgumentParser(
        prog="xlade cat",
        description="Display and inspect Lean or text files.",
        epilog=(
            "Examples: xlade cat File.lean --summary; "
            "xlade cat File.lean --diagnostics --explain; "
            "xlade cat --experiment exp-006-teorth-analysis"
        ),
    )
    parser.add_argument("files", nargs="*", help="file paths, or paths relative to --experiment")
    parser.add_argument("-n", "--number", action="store_true", help="number all output lines")
    parser.add_argument("-b", "--number-nonblank", action="store_true", help="number non-blank lines")
    parser.add_argument("-s", "--squeeze-blank", action="store_true", help="suppress repeated blank lines")
    parser.add_argument("-E", "--show-ends", action="store_true", help="show `$` at the end of each line")
    parser.add_argument("-T", "--show-tabs", action="store_true", help="show tab characters as `^I`")
    parser.add_argument("-v", "--show-nonprinting", action="store_true", help="show non-printing characters")
    parser.add_argument("-A", "--show-all", action="store_true", help="equivalent to -vET")
    parser.add_argument("--head", type=int, metavar="N", help="show the first N lines")
    parser.add_argument("--tail", type=int, metavar="N", help="show the last N lines")
    parser.add_argument("--lines", type=parse_line_range, metavar="START-END", help="show an inclusive line range")
    parser.add_argument("--pager", action="store_true", help="send displayed text through a pager")
    parser.add_argument("--summary", action="store_true", help="show file metadata and Lean check status")
    parser.add_argument("--symbols", action="store_true", help="show declarations and their line numbers")
    parser.add_argument("--imports", action="store_true", help="show imported modules")
    parser.add_argument("--diagnostics", action="store_true", help="run Lean and show compiler diagnostics")
    parser.add_argument("--explain", action="store_true", help="add human explanations to Lean diagnostics")
    parser.add_argument("--context", type=int, metavar="LINE", help="show source around a one-based line number")
    parser.add_argument(
        "--context-lines",
        type=int,
        default=2,
        metavar="N",
        help="number of lines before and after --context (default: 2)",
    )
    parser.add_argument("--experiment", metavar="ID", help="resolve files inside experiments/ID")
    parser.add_argument("--all", action="store_true", help="inspect every Lean file in --experiment")
    return parser


def visible_text(text: str, show_tabs: bool, show_nonprinting: bool) -> str:
    """Render tabs and control characters in the familiar cat notation."""
    rendered = []
    for character in text:
        code = ord(character)
        if character == "\t" and show_tabs:
            rendered.append("^I")
        elif show_nonprinting and code < 32:
            rendered.append("^" + chr(code + 64))
        elif show_nonprinting and code == 127:
            rendered.append("^?")
        else:
            rendered.append(character)
    return "".join(rendered)


def select_lines(lines: list[str], args: argparse.Namespace) -> tuple[list[str], int]:
    """Select lines and return them with their original one-based start number."""
    total = len(lines)
    if args.head is not None:
        start, end = 1, args.head
    elif args.tail is not None:
        start, end = max(total - args.tail + 1, 1), total
    elif args.lines is not None:
        start, end = args.lines
    else:
        start, end = 1, total
    return lines[start - 1 : end], start


def read_lines(path: Path) -> list[str]:
    """Read a text file as logical lines."""
    with path.open("r", encoding="utf-8", newline="") as source:
        return source.read().splitlines()


def render_file(path: Path, args: argparse.Namespace) -> str:
    """Render one file according to the standard cat options."""
    lines = read_lines(path)
    selected, start = select_lines(lines, args)
    output = []
    blank_seen = False
    show_tabs = args.show_tabs or args.show_all
    show_nonprinting = args.show_nonprinting or args.show_all
    number_lines = args.number or args.number_nonblank
    for offset, line in enumerate(selected, start=start):
        is_blank = line == ""
        if args.squeeze_blank and is_blank and blank_seen:
            continue
        blank_seen = is_blank
        rendered = visible_text(line, show_tabs, show_nonprinting)
        if args.show_ends or args.show_all:
            rendered += "$"
        if number_lines and (args.number or not is_blank):
            rendered = f"{offset:>6}\t{rendered}"
        output.append(rendered)
    return "\n".join(output)


def imports_in(lines: list[str]) -> list[tuple[int, str]]:
    """Return imported modules and their source line numbers."""
    return [(number, match.group(1)) for number, line in enumerate(lines, 1) if (match := IMPORT_PATTERN.match(line))]


def symbols_in(lines: list[str]) -> list[tuple[int, str, str]]:
    """Return declaration kinds, names, and source line numbers."""
    symbols = []
    for number, line in enumerate(lines, 1):
        match = DECLARATION_PATTERN.match(line)
        if match:
            symbols.append((number, match.group(1), match.group(2)))
    return symbols


def run_lean(path: Path) -> tuple[int, str]:
    """Run Lean for one file and return its exit code and diagnostics."""
    if shutil.which("lean") is None:
        return 127, ""
    try:
        result = subprocess.run(["lean", str(path)], capture_output=True, text=True, check=False)
    except OSError as error:
        return 127, str(error)
    return result.returncode, result.stdout + result.stderr


def context_text(lines: list[str], line_number: int, radius: int) -> str:
    """Render numbered source around a target line."""
    start = max(line_number - radius, 1)
    end = min(line_number + radius, len(lines))
    return "\n".join(
        f"{'> ' if number == line_number else '  '}{number:>5} | {lines[number - 1]}"
        for number in range(start, end + 1)
    )


def summary_text(path: Path, lines: list[str], lean_status: tuple[int, str] | None) -> str:
    """Render a compact Lean file summary."""
    imports = imports_in(lines)
    symbols = symbols_in(lines)
    sorry_count = sum(line.count("sorry") for line in lines)
    output = [
        f"  File        {path}",
        f"  Lines       {len(lines)}",
        f"  Imports     {len(imports)}",
        f"  Symbols     {len(symbols)}",
        f"  sorry       {sorry_count}",
    ]
    if lean_status is not None:
        exit_code, diagnostics = lean_status
        status = "not found" if exit_code == 127 else "passed" if exit_code == 0 else "failed"
        output.append(f"  Lean        {status}")
        if exit_code not in (0, 127) and diagnostics:
            output.append(f"  Diagnostics {len(diagnostics.splitlines())} lines")
    return "\n".join(output)


def experiment_files(experiment: str) -> tuple[Path | None, list[Path]]:
    """Resolve an experiment and discover its Lean files."""
    root = Path("experiments") / experiment
    if not root.is_dir():
        return None, []
    return root, sorted(root.rglob("*.lean"))


def display(text: str, use_pager: bool) -> None:
    """Print content directly or send it through an available pager."""
    if use_pager:
        pager = shutil.which("less") or shutil.which("more")
        if pager:
            subprocess.run([pager], input=text + "\n", text=True, check=False)
            return
        print("xlade cat: no pager found; displaying output directly", file=sys.stderr)
    print(text, end="" if text.endswith("\n") else "\n")


def inspect_file(path: Path, args: argparse.Namespace) -> tuple[str, int]:
    """Build requested inspection output for one file."""
    lines = read_lines(path)
    sections = []
    lean_status = run_lean(path) if args.summary or args.diagnostics or args.explain else None
    if args.summary:
        sections.append(summary_text(path, lines, lean_status))
    if args.imports:
        imports = imports_in(lines)
        content = "\n".join(f"  {line:>5}  {name}" for line, name in imports) or "  [none]"
        sections.append("  Imports\n" + content)
    if args.symbols:
        symbols = symbols_in(lines)
        content = "\n".join(f"  {line:>5}  {kind:<10} {name}" for line, kind, name in symbols) or "  [none]"
        sections.append("  Symbols\n" + content)
    if args.context is not None:
        if args.context > len(lines):
            return f"xlade cat: {path}: line {args.context} is outside 1-{len(lines)}", 1
        sections.append(f"  Context: {path}:{args.context}\n{context_text(lines, args.context, args.context_lines)}")
    if args.diagnostics or args.explain:
        exit_code, diagnostics = lean_status or run_lean(path)
        if exit_code == 127:
            sections.append("  [error]  Lean was not found on PATH.")
        elif diagnostics:
            sections.append(f"  Diagnostics: {path}\n{diagnostics.rstrip()}")
            if args.explain:
                from tools.errors import explanations

                matches = explanations(diagnostics)
                content = "\n".join(f"  [hint]      {match}" for match in matches)
                sections.append(
                    "  Explanations\n" + (content or "  [info]      No matching human explanation rule found.")
                )
        else:
            sections.append("  [ok]      Lean completed without diagnostics.")
    if not sections:
        return render_file(path, args), 0
    return "\n\n".join(sections), 0


def run(arguments: list[str]) -> int:
    """Run the `xlade cat` command."""
    parser = build_parser()
    args = parser.parse_intermixed_args(arguments)
    for value in (args.head, args.tail, args.context_lines):
        if value is not None and value < 0:
            parser.error("line counts must be zero or greater")
    if args.context is not None and args.context < 1:
        parser.error("--context line must be greater than zero")
    if args.all and not args.experiment:
        parser.error("--all requires --experiment")
    if not args.files and not args.experiment:
        parser.error("provide a file or use --experiment")

    files = [Path(filename) for filename in args.files]
    if args.experiment:
        experiment_root, discovered = experiment_files(args.experiment)
        if experiment_root is None:
            print(f"xlade cat: experiment not found: {args.experiment}", file=sys.stderr)
            return 1
        if args.all:
            files = discovered
        elif files:
            files = [path if path.is_absolute() else experiment_root / path for path in files]
        else:
            if not discovered:
                print(f"xlade cat: no Lean files found in experiment {args.experiment}")
                return 0
            print(f"Lean files in experiments/{args.experiment}:")
            for path in discovered:
                print(f"  {path.relative_to(experiment_root)}")
            return 0

    rendered_files = []
    failures = 0
    for path in files:
        if not path.is_file():
            print(f"xlade cat: {path}: No such file or directory", file=sys.stderr)
            failures += 1
            continue
        try:
            rendered, status = inspect_file(path, args)
        except (OSError, UnicodeError) as error:
            print(f"xlade cat: {path}: {error}", file=sys.stderr)
            failures += 1
            continue
        rendered_files.append(rendered)
        failures += status

    if rendered_files:
        inspection_mode = any(
            (args.summary, args.symbols, args.imports, args.diagnostics, args.explain, args.context is not None)
        )
        display(("\n\n" if inspection_mode else "\n").join(rendered_files), args.pager)
    return 1 if failures else 0


def main() -> int:
    """Run the standalone cat entry point."""
    return run(sys.argv[1:])