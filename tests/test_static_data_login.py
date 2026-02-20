from selenium.webdriver.common.by import By
from utils.static_testdata import BASE_URL, VALID_USERNAME, VALID_PASSWORD


def test_static_data_login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    assert "secure area" in driver.page_source.lower()