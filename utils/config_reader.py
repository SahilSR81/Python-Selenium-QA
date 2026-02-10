import json
import os


def load_config(env="qa"):
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "config", "config.json")

    with open(config_path) as file:
        config = json.load(file)

    if env not in config:
        raise ValueError(f"Environment '{env}' not found in config.json")

    return config[env]
