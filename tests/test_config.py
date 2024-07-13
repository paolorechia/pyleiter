import pytest
from pyleiter.config import (
    _find_pyproject_toml,
    read_pyleiter_config,
)
from pyleiter.errors import PyleiterKeyNotFoundError


def test_find_pyproject_toml():
    """Checks that pyleiter successfully finds the pyproject.toml in same directory."""
    assert _find_pyproject_toml() == "pyproject.toml"


def test_pyleiter_extracts_correct_config(patch_config):
    assert read_pyleiter_config() == {
        "format": {
            "command": "ruff format",
            "help": "Applies ruff format to project",
        },
        "lint": {
            "command": "ruff check tests/conftest.py",
            "help": "Runs project formatter and linter",
        },
    }


@pytest.mark.nopatch_config
def test_pyleiter_complains_missing_config():
    with pytest.raises(PyleiterKeyNotFoundError):
        read_pyleiter_config()
