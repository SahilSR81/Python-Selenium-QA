from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver


def test_direct_access_blocked():
    driver = get_driver("chrome")
    driver.get("https://the-internet.herokuapp.com/secure")

    message = driver.find_element(By.ID, "flash").text
    driver.quit()

    assert "You must login" in message
