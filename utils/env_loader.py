import json
import os


def load_environment(env_name):
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "config", "env_profiles.json"
    )

    with open(config_path, "r") as f:
        data = json.load(f)

    if env_name not in data:
        raise ValueError(f"Environment '{env_name}' not found")

    return data[env_name]
