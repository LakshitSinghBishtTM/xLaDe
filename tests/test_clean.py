import os

from xlade.cli.clean import run


def test_clean_removes_project_local_state(initialized_project, fake_home, capsys):
    assert os.path.isdir(".xlade")
    run()
    captured = capsys.readouterr()
    assert not os.path.isdir(".xlade")
    assert "[deleted]  .xlade/" in captured.out


def test_clean_removes_global_state(tmp_project, fake_home, capsys):
    global_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(global_dir)
    run()
    captured = capsys.readouterr()
    assert not os.path.isdir(global_dir)
    assert "[deleted]  ~/.xlade/" in captured.out


def test_clean_reports_nothing_to_clean_when_empty(tmp_project, fake_home, capsys):
    run()
    captured = capsys.readouterr()
    assert "[skip]     .xlade/ not found" in captured.out
    assert "[skip]     ~/.xlade/ not found" in captured.out
    assert "Nothing to clean." in captured.out


def test_clean_reports_summary_count_for_both(initialized_project, fake_home, capsys):
    global_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(global_dir)
    run()
    captured = capsys.readouterr()
    assert "2 item(s) removed." in captured.out


def test_clean_reports_mixed_deleted_and_skip(initialized_project, fake_home, capsys):
    run()
    captured = capsys.readouterr()
    assert "[deleted]  .xlade/" in captured.out
    assert "[skip]     ~/.xlade/ not found" in captured.out
    assert "1 item(s) removed." in captured.out


def test_clean_does_not_touch_unrelated_files_in_cwd(initialized_project, fake_home):
    (initialized_project / "README.md").write_text("I don't know what to write\n")
    (initialized_project / "experiments").mkdir()
    run()
    assert os.path.isfile("README.md")
    assert os.path.isdir("experiments")
