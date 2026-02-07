import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.day22
def test_post_login_navigation(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open("https://www.saucedemo.com")
    login.login("standard_user", "secret_sauce")

    home.wait_for_url("inventory")
    assert home.get_page_title() == "Products"
