import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.config_reader import load_config


@pytest.fixture(params=["chrome", "firefox"])
def setup(request):
    browser = request.param
    config = load_config("qa")  # env decides URL + creds, NOT browser

    driver = get_driver(browser)
    driver.get(config["base_url"])

    yield driver, config
    driver.quit()


def test_login_using_json_config(setup):
    driver, config = setup

    driver.find_element(By.ID, "username").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    #  explicit wait for flash message
    message = (
        WebDriverWait(driver, 10)
        .until(EC.visibility_of_element_located((By.ID, "flash")))
        .text
    )

    assert "secure area" in message
