"""Tests for the xLaDe cat tool."""

from tools.files_extraction import cat


def make_file(tmp_path, content):
    path = tmp_path / "example.lean"
    path.write_text(content, encoding="utf-8")
    return path


def test_cat_displays_a_file(tmp_path, capsys):
    path = make_file(tmp_path, "first\nsecond\n")

    result = cat.run([str(path)])

    assert result == 0
    assert capsys.readouterr().out == "first\nsecond\n"


def test_cat_numbers_nonblank_lines(tmp_path, capsys):
    path = make_file(tmp_path, "first\n\nsecond\n")

    cat.run([str(path), "-b"])

    assert capsys.readouterr().out == "     1\tfirst\n\n     3\tsecond\n"


def test_cat_supports_line_range(tmp_path, capsys):
    path = make_file(tmp_path, "one\ntwo\nthree\n")

    cat.run([str(path), "--lines", "2-2"])

    assert capsys.readouterr().out == "two\n"


def test_cat_supports_multiple_files_and_intermixed_options(tmp_path, capsys):
    first = make_file(tmp_path, "first\n")
    second = tmp_path / "second.lean"
    second.write_text("second\n", encoding="utf-8")

    cat.run([str(first), "--head", "1", str(second)])

    assert capsys.readouterr().out == "first\nsecond\n"


def test_cat_reports_missing_file(capsys):
    result = cat.run(["missing.lean"])

    assert result == 1
    assert "No such file or directory" in capsys.readouterr().err


def test_cat_summary_imports_and_symbols(tmp_path, capsys):
    path = make_file(tmp_path, "import Mathlib\n\ndef add (a b : Nat) := a + b\n theorem demo : True := by trivial\n")

    cat.run([str(path), "--summary", "--imports", "--symbols"])

    output = capsys.readouterr().out
    assert "Lines" in output
    assert "Mathlib" in output
    assert "add" in output
    assert "demo" in output


def test_cat_context_marks_requested_line(tmp_path, capsys):
    path = make_file(tmp_path, "one\ntwo\nthree\nfour\n")

    cat.run([str(path), "--context", "3", "--context-lines", "1"])

    output = capsys.readouterr().out
    assert ">     3 | three" in output
    assert "      2 | two" in output


def test_cat_diagnostics_and_explanations(tmp_path, monkeypatch, capsys):
    path = make_file(tmp_path, "bad\n")
    monkeypatch.setattr(cat, "run_lean", lambda _: (1, "error: unknown identifier 'value'\n"))

    cat.run([str(path), "--diagnostics", "--explain"])

    output = capsys.readouterr().out
    assert "unknown identifier" in output
    assert "Lean cannot find this name" in output


def test_cat_lists_experiment_files(tmp_path, monkeypatch, capsys):
    experiment = tmp_path / "experiments" / "example"
    experiment.mkdir(parents=True)
    (experiment / "Main.lean").write_text("theorem demo : True := by trivial\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    result = cat.run(["--experiment", "example"])

    assert result == 0
    assert "Main.lean" in capsys.readouterr().out


def test_cat_reports_experiment_without_lean_files(tmp_path, monkeypatch, capsys):
    (tmp_path / "experiments" / "empty").mkdir(parents=True)
    monkeypatch.chdir(tmp_path)

    result = cat.run(["--experiment", "empty"])

    assert result == 0
    assert "no Lean files found" in capsys.readouterr().out
