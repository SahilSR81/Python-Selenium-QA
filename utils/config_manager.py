import os
import json


class ConfigManager:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.config_dir = os.path.join(self.base_dir, "config")

    def load_config(self, env="qa"):

        config_file = os.path.join(self.config_dir, f"{env}.json")

        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config not found: {env}")

        with open(config_file) as f:
            data = json.load(f)

        return data

    def validate_config(self, config):

        required_keys = {"base_url", "env_name"}

        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing config key: {key}")

        return True
