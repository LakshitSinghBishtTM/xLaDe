from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "sourceforge.yml"


def test_sourceforge_mirror_only_uses_main_as_its_source():
    """A feature branch must never be force-pushed to SourceForge main."""
    content = WORKFLOW.read_text()

    assert "push:\n    branches: [main]" in content
    assert "\n  create:" not in content
    assert "\n  delete:" not in content
    assert "if: github.ref == 'refs/heads/main'" in content
    assert "ref: refs/heads/main" in content
    assert "git push sourceforge HEAD:main" in content
    assert "git push --force sourceforge HEAD:main" not in content
