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


# ============================================================
# DAY 42 ADDITIONS — DATASET LAYER
# ============================================================


def load_dataset(dataset_name: str):
    """
    Generic dataset loader
    Example: load_dataset("test_login_dataset")
    """

    dataset_path = os.path.join(BASE_DIR, "data", f"{dataset_name}.json")

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found: {dataset_name}")

    with open(dataset_path, "r") as f:
        data = json.load(f)

    return data


def validate_dataset_structure(dataset):
    """
    Ensures dataset integrity
    """

    if not isinstance(dataset, list):
        raise ValueError("Dataset must be a list")

    for row in dataset:
        if not isinstance(row, dict):
            raise ValueError("Dataset rows must be dictionaries")

    return True
