import pytest

@pytest.mark.parametrize(
    "row",
    [
        {"username": "standard_user", "password": "secret_sauce"},
        {"username": "locked_out_user", "password": "secret_sauce"},
    ],
)
def test_login_dataset_execution(row):
    assert "username" in row
    assert "password" in row
