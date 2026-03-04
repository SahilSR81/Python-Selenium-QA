from utils.data_provider import load_dataset

def test_dataset_file_load():
    data = load_dataset("test_login_dataset")
    assert isinstance(data, list)
    assert len(data) > 0
