import pytest
import sys
from pyleiter.cli import main


@pytest.mark.parametrize(
    "command, expected_stdout",
    [
        (["pyleiter", "format"], "files left unchanged"),
        (["pyleiter", "lint"], "Running process ruff check tests/conftest.py"),
    ],
    ids=["format", "lint"],
)
def test_pyleiter(monkeypatch, capsys, command, expected_stdout):
    monkeypatch.setattr(sys, "argv", command)
    main()
    stdout = capsys.readouterr().out
    assert expected_stdout in stdout


def test_pyleiter_unrecognized_option(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["pyleiter", "undefined_command"])
    with pytest.raises(SystemExit):
        main()
    stderr = capsys.readouterr().err
    assert "invalid choice: 'undefined_command'" in stderr


def test_pyleiter_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["pyleiter", "-h"])
    with pytest.raises(SystemExit):
        main()
    stdout = capsys.readouterr().out
    stderr = capsys.readouterr().err

    assert "usage: " in stdout, f"stdout: {stdout}\nstderr: {stderr}"

    assert (
        "{format,lint}  {'format': 'Applies ruff format to project', 'lint': 'Runs project formatter and linter'}"
        in stdout
    )
