from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "mirror.yml"


def test_credentialed_mirror_workflow_is_limited_to_protected_main():
    """Mirror tokens must not be available to feature-branch workflow runs."""
    content = WORKFLOW.read_text()

    assert "push:\n    branches: [main]" in content
    assert "\n  create:" not in content
    assert "\n  delete:" not in content
    assert "if: github.ref == 'refs/heads/main'" in content

    for secret in (
        "GITLAB_TOKEN",
        "CODEBERG_TOKEN",
        "BITBUCKET_TOKEN",
        "GITEA_TOKEN",
    ):
        assert f"secrets.{secret}" in content
