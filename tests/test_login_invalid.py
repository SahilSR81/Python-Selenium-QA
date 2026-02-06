import pytest
from pages.login_page import LoginPage


@pytest.mark.day21
@pytest.mark.parametrize(
    "username,password",
    [("standard_user", "wrong_pass"), ("wrong_user", "secret_sauce"), ("", "")],
)
def test_invalid_login(driver, username, password):
    login = LoginPage(driver)

    login.login(username, password)

    error_msg = login.get_error_message()
    assert "Epic sadface" in error_msg
