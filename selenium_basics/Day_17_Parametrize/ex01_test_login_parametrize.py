import pytest

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "admin123", True),
        ("admin", "wrong", False),
        ("wrong", "admin123", False),
        ("", "admin123", False),
        ("admin", "", False),
    ]
)
def test_login(username, password, expected):
    """
    Simulated login logic using parametrize
    """

    valid_user = "admin"
    valid_pass = "admin123"

    result = (username == valid_user and password == valid_pass)

    assert result == expected


if __name__ == "__main__":
    print("Day 17 login parametrize tests executed.")

