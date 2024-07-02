import subprocess

def test_pyleiter():
    assert subprocess.run(["python", "-m", "pyleiter"], capture_output=True).stdout.decode() == "hello world\n"