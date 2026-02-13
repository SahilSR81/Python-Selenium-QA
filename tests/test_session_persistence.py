import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
from utils.config_reader import load_config


@pytest.fixture
def driver():
    config = load_config("qa")
    driver = get_driver("chrome")
    driver.get(config["base_url"])
    yield driver
    driver.quit()


def test_session_persistence_after_navigation(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    driver.get("https://the-internet.herokuapp.com/secure")

    assert "Secure Area" in driver.page_source
