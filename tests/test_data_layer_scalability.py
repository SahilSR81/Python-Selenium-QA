def test_data_layer_structure(valid_login_data, invalid_login_data):
    assert isinstance(valid_login_data, list)
    assert isinstance(invalid_login_data, list)
    assert len(valid_login_data) >= 1
    assert len(invalid_login_data) >= 1
