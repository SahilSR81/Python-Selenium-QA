import time
from utils.browser_runner import run_on_all_browsers


def basic_screenshot_test(driver):
    browser = driver.capabilities["browserName"]
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    driver.get("https://example.com")
    driver.save_screenshot(f"screenshots/{browser}_{timestamp}.png")


def test_basic_screenshot():
    run_on_all_browsers(basic_screenshot_test)


if __name__ == "__main__":
    test_basic_screenshot()
    print("All tests passed.")
