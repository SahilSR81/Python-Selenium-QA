import configparser
import os


class IniConfigManager:

    @staticmethod
    def load(env="QA"):
        project_root = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(project_root, "config", "framework_config.ini")

        if not os.path.exists(config_path):
            raise FileNotFoundError("framework_config.ini not found")

        config = configparser.ConfigParser()
        config.read(config_path)

        if env not in config:
            raise ValueError(f"Environment '{env}' not found in ini file")

        return config[env]
