import pytest
import time
from utils.wait_utils import wait_visible
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_smoke_screenshot(driver):
    driver.get("https://example.com")

    heading = wait_visible(driver, (By.TAG_NAME, "h1"))
    assert heading.text == "Example Domain"

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/smoke_{timestamp}.png")
