def test_environment_timeout_positive(env_config):
    assert env_config["timeout"] > 0
