def test_config_values(config_manager):

    assert config_manager["env_name"] == "qa"
