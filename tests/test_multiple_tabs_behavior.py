from utils.driver_factory import get_driver


def test_multiple_tabs_session_consistency():
    driver = get_driver("chrome")
    driver.get("https://the-internet.herokuapp.com/login")

    driver.execute_script("window.open('https://the-internet.herokuapp.com/');")

    handles = driver.window_handles
    assert len(handles) == 2

    driver.switch_to.window(handles[1])
    assert "The Internet" in driver.title

    driver.quit()
