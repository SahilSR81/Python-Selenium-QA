import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.day21
def test_logout(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.login("standard_user", "secret_sauce")
    assert home.get_page_title() == "Products"

    home.logout()
    assert "saucedemo.com" in driver.current_url
