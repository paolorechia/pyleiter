import pytest
import sys
from pyleiter.cli import main

# def test_pyleiter():
#     process = subprocess.run(
#         ["python", "-m", "pyleiter", "format"], capture_output=True
#     )
#     stdout = process.stdout.decode()
#     stderr = process.stderr.decode()
#     assert stdout == "", stderr


def test_pyleiter_unrecognized_option(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["pyleiter", "undefined_command"])
    with pytest.raises(SystemExit):
        main()
    stderr = capsys.readouterr().err
    assert "unrecognized arguments: undefined_command" in stderr


def test_pyleiter_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["python", "-m", "pyleiter", "-h"])
    with pytest.raises(SystemExit):
        main()
    stdout = capsys.readouterr().out
    stderr = capsys.readouterr().err
    assert (
        "usage: " in stdout or "usage:" in stdout
    ), f"stdout: {stdout}\nstderr: {stderr}"
