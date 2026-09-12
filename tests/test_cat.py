"""Tests for the xLaDe cat tool."""

from tools import cat


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
