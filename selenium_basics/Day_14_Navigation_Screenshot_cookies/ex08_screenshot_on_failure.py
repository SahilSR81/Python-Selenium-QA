import time
from selenium.webdriver.common.by import By
from utils.browser_runner import run_on_all_browsers


def screenshot_on_failure_test(driver):
    browser = driver.capabilities["browserName"]
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    driver.get("https://example.com")

    try:
        driver.find_element(By.ID, "does_not_exist").click()
    except Exception:
        driver.save_screenshot(f"screenshots/{browser}_failure_{timestamp}.png")


def test_screenshot_on_failure():
    run_on_all_browsers(screenshot_on_failure_test)


if __name__ == "__main__":
    test_screenshot_on_failure()
    print("All tests passed.")
