import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.config_reader import load_config
from utils.logger_config import get_logger

logger = get_logger("LoginTest")


@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup(request):
    browser = request.param
    config = load_config("qa")

    logger.info(f"Launching browser: {browser}")

    driver = get_driver(browser)
    driver.get(config["base_url"])

    yield driver, config
    logger.info("Closing browser")
    driver.quit()


def test_login_with_logging(setup):
    driver, config = setup

    logger.info("Entering username")
    driver.find_element(By.ID, "username").send_keys(config["username"])

    logger.info("Entering password")
    driver.find_element(By.ID, "password").send_keys(config["password"])

    logger.info("Clicking login button")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    logger.info("Waiting for success message")
    message = (
        WebDriverWait(driver, 10)
        .until(EC.visibility_of_element_located((By.ID, "flash")))
        .text
    )

    logger.info("Validating login success")
    assert "secure area" in message

    logger.info("Login test passed successfully")
