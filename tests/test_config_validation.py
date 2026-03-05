from utils.config_manager import ConfigManager


def test_config_validation():

    manager = ConfigManager()

    config = {"env_name": "qa", "base_url": "https://example.com"}

    assert manager.validate_config(config) is True
