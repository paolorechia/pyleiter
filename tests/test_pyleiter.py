import subprocess


def test_pyleiter(patch_config):
    assert (
        subprocess.run(
            ["python", "-m", "pyleiter", "format"], capture_output=True
        ).stdout.decode()
        == "hello world\n"
    )


def test_pyleiter_help(patch_config):
    help_msg = subprocess.run(
        ["python", "-m", "pyleiter", "-h"], capture_output=True
    ).stdout.decode()
    assert "usage: " in help_msg
