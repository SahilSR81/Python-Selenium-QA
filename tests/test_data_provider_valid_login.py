import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_valid_users_from_provider(driver, valid_login_data):
    driver.get("https://the-internet.herokuapp.com/login")

    for user in valid_login_data:
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()

        driver.find_element(By.ID, "username").send_keys(user["username"])
        driver.find_element(By.ID, "password").send_keys(user["password"])
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        assert "secure area" in driver.page_source.lower()

        driver.get("https://the-internet.herokuapp.com/login")
