import pytest
from utils.wait_utils import wait_clickable
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_regression_navigation(driver):
    driver.get("https://the-internet.herokuapp.com")

    link = wait_clickable(driver, (By.LINK_TEXT, "A/B Testing"))
    link.click()

    assert "A/B Test" in driver.page_source
