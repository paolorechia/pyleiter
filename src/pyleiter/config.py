import os
import toml

from pyleiter.errors import PyProjectTomlNotFoundError


def find_pyproject_toml():
    cwd = os.getcwd()
    cwd_files = os.listdir("./")
    if "pyproject.toml" not in cwd_files:
        return PyProjectTomlNotFoundError(
            f"File 'pyproject.toml' not found in path {cwd}"
        )
    else:
        return "pyproject.toml"


def parse_config_file(filepath):
    with open(filepath, "r") as fd:
        return toml.load(fd)


def get_pyleiter_config(config: dict):
    return config.get("pyleiter", {})
