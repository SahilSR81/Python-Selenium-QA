from utils.driver_factory import get_driver


def test_cookie_storage():
    driver = get_driver("chrome")
    driver.get("https://the-internet.herokuapp.com/")

    driver.add_cookie({"name": "automation_cookie", "value": "active"})

    cookie = driver.get_cookie("automation_cookie")

    assert cookie is not None, "Cookie was not set"
    assert cookie["value"] == "active"

    driver.quit()
