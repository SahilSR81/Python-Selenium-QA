from selenium.webdriver.common.by import By


def test_day_19_intentional_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    # INTENTIONAL FAILURE
    driver.find_element(By.ID, "username_WRONG").send_keys("admin")
