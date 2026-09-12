"""Display xLaDe files with Linux-style cat options."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_line_range(value: str) -> tuple[int, int]:
    """Parse a one-based inclusive line range such as `10-25`."""
    try:
        start_text, end_text = value.split("-", 1)
        start = int(start_text)
        end = int(end_text)
    except ValueError as error:
        raise argparse.ArgumentTypeError("line range must look like START-END") from error

    if start < 1 or end < start:
        raise argparse.ArgumentTypeError("line range must start at 1 and end after START")

    return start, end


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for `xlade cat`."""
    parser = argparse.ArgumentParser(
        prog="xlade cat",
        description="Display one or more xLaDe files.",
    )
    parser.add_argument("files", nargs="+", help="file paths to display")
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


def render_file(path: Path, args: argparse.Namespace, next_line: int) -> tuple[str, int]:
    """Render one file and return its output with the next global line number."""
    with path.open("r", encoding="utf-8", newline="") as source:
        lines = source.read().splitlines()

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

    if output and (args.head is not None or args.tail is not None or args.lines is not None):
        output.append("")

    return "\n".join(output), next_line + len(output)


def display(text: str, use_pager: bool) -> None:
    """Print content directly or send it through an available pager."""
    if use_pager:
        pager = shutil.which("less") or shutil.which("more")
        if pager:
            subprocess.run([pager], input=text + "\n", text=True, check=False)
            return
        print("xlade cat: no pager found; displaying output directly", file=sys.stderr)

    print(text, end="" if text.endswith("\n") else "\n")


def run(arguments: list[str]) -> int:
    """Run the `xlade cat` command."""
    parser = build_parser()
    args = parser.parse_intermixed_args(arguments)

    for value in (args.head, args.tail):
        if value is not None and value < 0:
            parser.error("line counts must be zero or greater")

    rendered_files = []
    failures = 0
    next_line = 1

    for filename in args.files:
        path = Path(filename)
        if not path.is_file():
            print(f"xlade cat: {filename}: No such file or directory", file=sys.stderr)
            failures += 1
            continue

        try:
            rendered, next_line = render_file(path, args, next_line)
        except OSError as error:
            print(f"xlade cat: {filename}: {error}", file=sys.stderr)
            failures += 1
            continue
        rendered_files.append(rendered)

    if rendered_files:
        display("\n".join(rendered_files), args.pager)

    return 1 if failures else 0


def main() -> int:
    """Run the standalone cat entry point."""
    return run(sys.argv[1:])
