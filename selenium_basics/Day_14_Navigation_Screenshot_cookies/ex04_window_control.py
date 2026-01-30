import time
from utils.browser_runner import run_on_all_browsers


def window_control_test(driver):
    driver.get("https://example.com")

    driver.set_window_size(900, 600)
    time.sleep(1)

    driver.maximize_window()
    time.sleep(1)

    driver.minimize_window()
    time.sleep(1)


def test_window_control():
    run_on_all_browsers(window_control_test)


if __name__ == "__main__":
    test_window_control()
    print("All tests passed.")
