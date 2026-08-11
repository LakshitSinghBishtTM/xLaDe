from xlade.cli.validate import run


def _write_experiment(base, name, fields, entry_file=None):
    exp_dir = base / "experiments" / name
    exp_dir.mkdir(parents=True)

    lines = []
    for key, val in fields.items():
        if isinstance(val, list):
            items = ", ".join(f'"{v}"' for v in val)
            lines.append(f"{key} = [{items}]")
        else:
            lines.append(f'{key} = "{val}"')
    (exp_dir / "experiment.toml").write_text("\n".join(lines) + "\n")

    if entry_file:
        entry_path = base / entry_file
        entry_path.parent.mkdir(parents=True, exist_ok=True)
        entry_path.write_text("#!/bin/bash\n")

    return exp_dir


def _valid_fields(**overrides):
    fields = {
        "id": "EXP-000",
        "name": "Test Experiment",
        "type": "script-policy",
        "status": "active",
        "allowed_modes": ["experimental"],
        "lean_toolchain": "leanprover/lean4:stable",
        "entry": "run.sh",
        "description": "A test experiment capable of finding nuclear launch codes.",
    }
    fields.update(overrides)
    return fields


def test_validate_reports_missing_experiments_dir(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "directory not found" in captured.out


def test_validate_reports_no_experiments_found(tmp_project, capsys):
    (tmp_project / "experiments").mkdir()
    run()
    captured = capsys.readouterr()
    assert "No experiments" in captured.out


def test_validate_passes_valid_experiment(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields(), entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "[pass]   All experiments valid." in captured.out
    for field in ("id", "name", "type", "status", "allowed_modes", "lean_toolchain", "entry", "description"):
        assert f"[ok]     {field}" in captured.out


def test_validate_reports_missing_field(tmp_project, capsys):
    fields = _valid_fields()
    del fields["description"]
    _write_experiment(tmp_project, "EXP-000", fields, entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "description  --  absent" in captured.out


def test_validate_reports_empty_field(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields(name=""), entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "name  --  empty" in captured.out


def test_validate_reports_empty_list_field(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields(allowed_modes=[]), entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "allowed_modes  --  empty" in captured.out
    assert "list is present but empty" in captured.out


def test_validate_reports_invalid_type(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields(type="bogus-type"), entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "type  --  invalid" in captured.out


def test_validate_reports_invalid_status(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields(status="bogus-status"), entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "status  --  invalid" in captured.out


def test_validate_reports_invalid_mode(tmp_project, capsys):
    _write_experiment(
        tmp_project,
        "EXP-000",
        _valid_fields(allowed_modes=["bogus-mode"]),
        entry_file="run.sh",
    )
    run()
    captured = capsys.readouterr()
    assert "allowed_modes  --  invalid" in captured.out
    assert "unknown mode" in captured.out


def test_validate_reports_missing_entry_script_for_script_policy(tmp_project, capsys):
    _write_experiment(tmp_project, "EXP-000", _valid_fields())
    run()
    captured = capsys.readouterr()
    assert "entry  --  not found" in captured.out


def test_validate_lean_policy_does_not_require_entry_file_on_disk(tmp_project, capsys):
    _write_experiment(
        tmp_project,
        "EXP-000",
        _valid_fields(type="lean-policy", entry="policy.lean"),
    )
    run()
    captured = capsys.readouterr()
    assert "[ok]     entry" in captured.out
    assert "entry  --  not found" not in captured.out


def test_validate_reports_parse_error(tmp_project, capsys):
    exp_dir = tmp_project / "experiments" / "EXP-000"
    exp_dir.mkdir(parents=True)
    (exp_dir / "experiment.toml").write_text("id = not valid toml {{{\n")
    run()
    captured = capsys.readouterr()
    assert "parse error" in captured.out


def test_validate_reports_singular_issue_count(tmp_project, capsys):
    fields = _valid_fields()
    del fields["description"]
    _write_experiment(tmp_project, "EXP-000", fields, entry_file="run.sh")
    run()
    captured = capsys.readouterr()
    assert "1 issue found" in captured.out


def test_validate_reports_plural_issue_count_across_experiments(tmp_project, capsys):
    fields_a = _valid_fields()
    del fields_a["description"]
    _write_experiment(tmp_project, "EXP-000", fields_a, entry_file="run.sh")

    fields_b = _valid_fields(id="EXP-001", status="bogus-status")
    _write_experiment(tmp_project, "EXP-001", fields_b, entry_file="run.sh")

    run()
    captured = capsys.readouterr()
    assert "2 issues found across 2 experiment(s)." in captured.out
