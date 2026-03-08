import pytest
def test_impact_flag(pytestconfig):
    flag = pytestconfig.getoption("--impact")
    assert flag in [True, False]
