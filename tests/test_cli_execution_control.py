import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_login_smoke(setup_cli):
    driver, config = setup_cli

    driver.find_element(By.ID, "username").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    message = (
        WebDriverWait(driver, 10)
        .until(EC.visibility_of_element_located((By.ID, "flash")))
        .text
    )

    assert "secure area" in message


@pytest.mark.regression
def test_page_title_regression(setup_cli):
    driver, _ = setup_cli
    assert "The Internet" in driver.title
