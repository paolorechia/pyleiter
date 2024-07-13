from unittest import mock
import pytest


@pytest.fixture(autouse=False)
def patch_config():
    """Patches pyproject with test file."""
    with mock.patch(
        "pyleiter.config._find_pyproject_toml", return_value="tests/test_pyproject.toml"
    ):
        yield
