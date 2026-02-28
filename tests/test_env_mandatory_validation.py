def test_environment_profile_mandatory(pytestconfig):
    env = pytestconfig.getoption("--env")
    assert env in ["dev", "qa", "prod"]
