#!/usr/bin/env python3
"""Run Lean and explain common errors using a local SQLite database."""

from __future__ import annotations

import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("error_rules.sqlite3")
SCHEMA_PATH = Path(__file__).with_name("error_rules.sql")
SEPARATOR = "-" * 100


def open_database() -> sqlite3.Connection:
    """Open the local rules database and create it from the SQL file if needed."""
    database = sqlite3.connect(DATABASE_PATH)
    database.row_factory = sqlite3.Row

    if not database.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'error_rules'").fetchone():
        database.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        database.commit()

    return database


def run_lean(lean_file: str) -> tuple[int, str]:
    """Run Lean and return its exit code together with all diagnostic text."""
    if shutil.which("lean") is None:
        return 127, ""

    try:
        result = subprocess.run(
            ["lean", lean_file],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as error:
        return 127, f"Could not start Lean: {error}\n"

    # Lean may write diagnostics to either stream, so preserve both.
    return result.returncode, result.stdout + result.stderr


def explanations(output: str) -> list[str]:
    """Read matching explanations from the local database."""
    lowered_output = output.lower()
    found = []

    with open_database() as database:
        rules = database.execute("SELECT phrase, explanation FROM error_rules ORDER BY length(phrase) DESC").fetchall()

    matching_phrases = [rule["phrase"].lower() for rule in rules if rule["phrase"].lower() in lowered_output]

    for rule in rules:
        phrase = rule["phrase"].lower()
        more_specific_match = any(phrase != other and phrase in other for other in matching_phrases)
        if phrase in matching_phrases and not more_specific_match:
            found.append(rule["explanation"])

    return found


def main() -> int:
    if len(sys.argv) != 2:
        print("  Usage: lean-error-hints.py <lean-file>")
        return 1

    print()
    print("  xLaDe Lean Error Humanizer")
    print(f"  {SEPARATOR}")
    print(f"  File        {sys.argv[1]}")

    exit_code, output = run_lean(sys.argv[1])
    if exit_code == 127:
        print(f"  {SEPARATOR}")
        print("  [error]  Lean was not found on PATH.")
        print("           Install Lean through elan, then run this tool again.")
        print()
        return exit_code

    print(f"  {SEPARATOR}")
    if output:
        print(output, end="")

        matches = explanations(output)
        print(f"  {SEPARATOR}")
        if matches:
            print("  Human explanations")
            for explanation in matches:
                print(f"  [hint]   {explanation}")
        else:
            print("  [info]   No matching human explanation rule found.")
    elif exit_code == 0:
        print("  [ok]     Lean completed without diagnostics.")
    else:
        print("  [error]  Lean returned an error without diagnostic text.")

    print(f"  {SEPARATOR}")
    print(f"  Status: {'success' if exit_code == 0 else 'failed'}")
    print()

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
