from unittest import mock
import pytest


@pytest.fixture(autouse=True)
def patch_config(request):
    """Patches pyproject with test file."""
    if "nopatch_config" in request.keywords:
        yield
    else:
        with mock.patch(
            "pyleiter.config._find_pyproject_toml",
            return_value="tests/test_pyproject.toml",
        ):
            yield
