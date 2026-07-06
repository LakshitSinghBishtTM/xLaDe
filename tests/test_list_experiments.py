from xlade.cli.list_experiments import run


def test_list_no_experiments_dir(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "No experiments" in captured.out


def test_list_empty_experiments_dir(tmp_project, capsys):
    (tmp_project / "experiments").mkdir()
    run()
    captured = capsys.readouterr()
    assert "No valid experiments found" in captured.out


def test_list_shows_experiment(experiments_dir, capsys):
    run()
    captured = capsys.readouterr()
    assert "EXP-001" in captured.out


def test_list_shows_status(experiments_dir, capsys):
    run()
    captured = capsys.readouterr()
    assert "active" in captured.out


def test_list_shows_mode(experiments_dir, capsys):
    run()
    captured = capsys.readouterr()
    assert "experimental" in captured.out
