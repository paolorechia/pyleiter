import pytest
from unittest import mock
from pyleiter.config import (
    _find_pyproject_toml,
    read_pyleiter_config,
)
from pyleiter.errors import PyleiterKeyNotFoundError


def test_find_pyproject_toml():
    """Checks that pyleiter successfully finds the pyproject.toml in same directory."""
    assert _find_pyproject_toml() == "pyproject.toml"


def test_pyleiter_extracts_correct_config():
    with mock.patch(
        "pyleiter.config._find_pyproject_toml", return_value="tests/test_pyproject.toml"
    ):
        assert read_pyleiter_config() == {
            "lint": {
                "command": "ruff format && ruff check src && ruff check tests",
                "help": "Runs project formatter and linter",
            }
        }


def test_pyleiter_complains_missing_config():
    with pytest.raises(PyleiterKeyNotFoundError):
        read_pyleiter_config()
