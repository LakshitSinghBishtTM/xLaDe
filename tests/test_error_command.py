"""Tests for the database-backed `xlade error` command."""

from tools.errors import humanize


def test_humanize_uses_the_error_database():
    output = humanize("unknown identifier 'value'")

    assert "Lean cannot find this name" in output
