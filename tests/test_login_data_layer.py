import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.testdata_manager import TestDataManager
from utils.config_reader import load_config


@pytest.fixture(params=["chrome", "firefox"])
def setup(request):
    browser = request.param
    config = load_config("qa")

    driver = get_driver(browser)
    driver.get(config["base_url"])

    yield driver
    driver.quit()


@pytest.mark.parametrize("data", TestDataManager.load("login", "valid_users.json"))
def test_valid_login_data_layer(setup, data):
    driver = setup

    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    message = (
        WebDriverWait(driver, 10)
        .until(EC.visibility_of_element_located((By.ID, "flash")))
        .text
    )

    assert data["expected"] in message


@pytest.mark.parametrize("data", TestDataManager.load("login", "invalid_users.json"))
def test_invalid_login_data_layer(setup, data):
    driver = setup

    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    message = (
        WebDriverWait(driver, 10)
        .until(EC.visibility_of_element_located((By.ID, "flash")))
        .text
    )

    assert data["expected"] in message
