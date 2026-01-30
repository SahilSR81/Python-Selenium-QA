import time
from selenium.webdriver.common.by import By
from utils.browser_runner import run_on_all_browsers


def screenshot_after_action_test(driver):
    browser = driver.capabilities["browserName"]
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.save_screenshot(f"screenshots/{browser}_after_action_{timestamp}.png")


def test_screenshot_after_action():
    run_on_all_browsers(screenshot_after_action_test)


if __name__ == "__main__":
    test_screenshot_after_action()
    print("All tests passed.")
