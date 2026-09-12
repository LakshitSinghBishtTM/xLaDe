"""Database-backed helpers for translating Lean diagnostics."""

from __future__ import annotations

import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("error_rules.sqlite3")
SCHEMA_PATH = Path(__file__).with_name("error_rules.sql")


def open_database() -> sqlite3.Connection:
    """Open the local rule database and initialise it when needed."""
    database = sqlite3.connect(DATABASE_PATH)
    database.row_factory = sqlite3.Row

    table = database.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'error_rules'").fetchone()
    if table is None:
        database.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        database.commit()

    return database


def explanations(error_text: str) -> list[str]:
    """Return the most specific explanations matching a Lean diagnostic."""
    lowered_text = error_text.lower()

    with open_database() as database:
        rules = database.execute("SELECT phrase, explanation FROM error_rules").fetchall()

    matching_phrases = [rule["phrase"].lower() for rule in rules if rule["phrase"].lower() in lowered_text]
    found = []
    for rule in rules:
        phrase = rule["phrase"].lower()
        more_specific_match = any(phrase != other and phrase in other for other in matching_phrases)
        if phrase in matching_phrases and not more_specific_match:
            found.append(rule["explanation"])

    return found


def humanize(error_text: str) -> str:
    """Format a Lean diagnostic and its database explanations for the CLI."""
    matches = explanations(error_text)
    lines = [f"  Lean error  {error_text}"]
    if matches:
        lines.append("  Explanations")
        lines.extend(f"  [hint]      {explanation}" for explanation in matches)
    else:
        lines.append("  [info]      No matching human explanation rule found.")
    return "\n".join(lines)
