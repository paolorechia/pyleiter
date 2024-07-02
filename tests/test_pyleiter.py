import subprocess


def test_pyleiter():
    assert (
        subprocess.run(
            ["python", "-m", "pyleiter"], capture_output=True
        ).stdout.decode()
        == "hello world\n"
    )


def test_pyleiter_help():
    help_msg = subprocess.run(
        ["python", "-m", "pyleiter", "-h"], capture_output=True
    ).stdout.decode()
    assert "usage: " in help_msg
