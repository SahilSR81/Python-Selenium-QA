def test_dataset_has_required_fields(login_dataset):
    required = {"username", "password", "expected"}

    for row in login_dataset:
        assert required.issubset(row.keys())
