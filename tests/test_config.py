from pyleiter.config import find_pyproject_toml


def test_find_pyproject_toml():
    assert find_pyproject_toml() == "pyproject.toml"
