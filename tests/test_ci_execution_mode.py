def test_ci_headless_required(pytestconfig):
    headless = pytestconfig.getoption("--headless")
    assert isinstance(headless, bool)
