import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_invalid_users_from_provider(driver, invalid_login_data):
    driver.get("https://the-internet.herokuapp.com/login")

    for user in invalid_login_data:
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()

        driver.find_element(By.ID, "username").send_keys(user["username"])
        driver.find_element(By.ID, "password").send_keys(user["password"])
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        flash = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "invalid" in flash.text.lower()

        driver.get("https://the-internet.herokuapp.com/login")
