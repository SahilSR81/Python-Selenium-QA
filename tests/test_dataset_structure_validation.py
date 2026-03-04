from utils.data_provider import validate_dataset_structure


def test_dataset_validation_pass():
    dataset = [{"username": "user", "password": "pass"}]
    assert validate_dataset_structure(dataset) is True
