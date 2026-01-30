import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_runner import run_on_all_browsers


def login_flow_test(driver):
    browser = driver.capabilities["browserName"]
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
        "tomsmith"
    )
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    driver.save_screenshot(f"screenshots/{browser}_login_{timestamp}.png")


def test_login_flow():
    run_on_all_browsers(login_flow_test)


if __name__ == "__main__":
    test_login_flow()
    print("All tests passed.")
