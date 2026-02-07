import pytest
from pages.login_page import LoginPage


@pytest.mark.day22
def test_login_button_still_enabled_after_failure(driver):
    login = LoginPage(driver)
    login.open("https://www.saucedemo.com")

    login.login("wrong_user", "wrong_pass")

    assert login.is_login_button_enabled()
