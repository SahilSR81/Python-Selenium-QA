def test_dashboard_loaded_after_login(driver):
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.login("standard_user", "secret_sauce")

    assert dashboard.is_dashboard_loaded()
