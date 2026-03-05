def test_config_fixture(config_manager):

    assert "env_name" in config_manager
    assert "base_url" in config_manager
