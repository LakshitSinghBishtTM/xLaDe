"""Tests for the optional Lean error humanizer tool."""

import importlib.util
from pathlib import Path

TOOL_PATH = Path(__file__).parents[1] / "tools" / "errors" / "lean-error-hints.py"
SPEC = importlib.util.spec_from_file_location("lean_error_hints", TOOL_PATH)
humanizer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(humanizer)


def configure_test_database(tmp_path, monkeypatch):
    """Use a temporary database while testing the rule reader."""
    schema_path = tmp_path / "error_rules.sql"
    database_path = tmp_path / "error_rules.sqlite3"
    schema_path.write_text(
        """
    CREATE TABLE error_rules (phrase TEXT PRIMARY KEY, explanation TEXT NOT NULL);
    INSERT INTO error_rules VALUES
      ('type mismatch', 'Check the expected and actual types.'),
      ('application type mismatch', 'Check the function argument type.'),
      ('unknown identifier', 'Check the name and its imports.');
    """,
        encoding="utf-8",
    )
    monkeypatch.setattr(humanizer, "DATABASE_PATH", database_path)
    monkeypatch.setattr(humanizer, "SCHEMA_PATH", schema_path)


def test_explanations_are_loaded_from_database(tmp_path, monkeypatch):
    configure_test_database(tmp_path, monkeypatch)

    result = humanizer.explanations("unknown identifier: value")

    assert result == ["Check the name and its imports."]


def test_specific_rule_suppresses_generic_rule(tmp_path, monkeypatch):
    configure_test_database(tmp_path, monkeypatch)

    result = humanizer.explanations("application type mismatch")

    assert result == ["Check the function argument type."]


def test_main_reports_lean_missing(monkeypatch, capsys):
    monkeypatch.setattr(humanizer, "run_lean", lambda _: (127, ""))
    monkeypatch.setattr(humanizer.sys, "argv", ["lean-error-hints.py", "Example.lean"])

    result = humanizer.main()
    output = capsys.readouterr().out

    assert result == 127
    assert "xLaDe Lean Error Humanizer" in output
    assert "[error]  Lean was not found on PATH." in output


def test_main_returns_lean_status_and_prints_hint(monkeypatch, capsys):
    monkeypatch.setattr(
        humanizer,
        "run_lean",
        lambda _: (1, "error: unknown identifier 'value'\n"),
    )
    monkeypatch.setattr(humanizer, "explanations", lambda _: ["Check the name and its imports."])
    monkeypatch.setattr(humanizer.sys, "argv", ["lean-error-hints.py", "Example.lean"])

    result = humanizer.main()
    output = capsys.readouterr().out

    assert result == 1
    assert "[hint]   Check the name and its imports." in output
    assert "Status: failed" in output
