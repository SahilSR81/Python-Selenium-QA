import pytest

def test_ci_flag_available(pytestconfig):
    assert pytestconfig.getoption("--ci-mode") in [True, False]
