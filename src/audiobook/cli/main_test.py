"""Tests for the CLI entry point."""

from typer.testing import CliRunner

from audiobook.cli.main import app


def test_help_exits_zero() -> None:
    """Invoking --help should succeed with exit code 0."""
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
