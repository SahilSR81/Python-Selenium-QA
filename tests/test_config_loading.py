from utils.config_manager import ConfigManager


def test_config_file_load():

    manager = ConfigManager()

    config = manager.load_config("qa")

    assert isinstance(config, dict)
