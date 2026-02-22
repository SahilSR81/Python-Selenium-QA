def test_environment_profile_loaded(env_config):
    assert "base_url" in env_config
    assert "timeout" in env_config
