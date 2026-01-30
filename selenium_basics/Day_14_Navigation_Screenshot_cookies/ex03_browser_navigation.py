from utils.browser_runner import run_on_all_browsers
import time


def browser_navigation_test(driver):
    driver.get("https://google.com")
    time.sleep(1)

    driver.get("https://bing.com")
    time.sleep(1)

    driver.back()
    time.sleep(1)

    driver.forward()
    time.sleep(1)

    driver.refresh()


def test_browser_navigation():
    run_on_all_browsers(browser_navigation_test)


if __name__ == "__main__":
    test_browser_navigation()
    print("All tests passed.")
