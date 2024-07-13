import pytest
import sys
from pyleiter.cli import main


def test_pyleiter(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["pyleiter", "format"])
    stdout = capsys.readouterr().out
    assert "files left unchanged" in stdout


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
    assert (
        "usage: " in stdout or "usage:" in stdout
    ), f"stdout: {stdout}\nstderr: {stderr}"
