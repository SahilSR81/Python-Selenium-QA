from utils.navigation_utils import open_url, get_current_url


def test_navigation_helper(driver):
    open_url(driver, "https://the-internet.herokuapp.com/")
    assert "the-internet" in get_current_url(driver)
