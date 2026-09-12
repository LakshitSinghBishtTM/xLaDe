"""Tests for the database-backed `xlade error` command."""

import sys

from tools.errors import humanize
from xlade.cli import main


def test_humanize_uses_the_error_database():
    output = humanize("unknown identifier 'value'")

    assert "Lean cannot find this name" in output


def test_cli_error_joins_error_arguments(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["xlade", "error", "type", "mismatch"])

    result = main.main()
    output = capsys.readouterr().out

    assert result == 0
    assert "Lean error  type mismatch" in output
    assert "different type" in output
