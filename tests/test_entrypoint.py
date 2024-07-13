import subprocess


def test_entrypoint():
    process = subprocess.run(["pyleiter", "-h"])
    process.stdout
