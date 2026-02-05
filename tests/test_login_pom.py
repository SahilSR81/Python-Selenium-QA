def test_valid_login_pom(driver):
    from pages.login_page import LoginPage
    from pages.home_page import HomePage

    login = LoginPage(driver)
    login.open("https://www.saucedemo.com")

    login.login("standard_user", "secret_sauce")

    home = HomePage(driver)
    assert home.get_page_title() == "Products"


def test_invalid_login_pom(driver):
    from pages.login_page import LoginPage

    login = LoginPage(driver)
    login.open("https://www.saucedemo.com")

    login.login("wrong_user", "wrong_pass")

    assert "Username and password do not match" in login.get_error_message()
