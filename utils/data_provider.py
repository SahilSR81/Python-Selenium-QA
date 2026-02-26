import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def load_login_data(user_type: str):
    """
    user_type: valid | invalid
    """

    file_map = {"valid": "valid_users.json", "invalid": "invalid_users.json"}

    if user_type not in file_map:
        raise ValueError(f"Unsupported user type: {user_type}")

    path = os.path.join(BASE_DIR, "testdata", "login", file_map[user_type])

    with open(path, "r") as f:
        return json.load(f)
