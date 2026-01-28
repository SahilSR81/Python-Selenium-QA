from utils.driver_factory import get_driver

BROWSERS = ["chrome", "firefox", "edge"]


def run_on_all_browsers(test_logic):
    for browser in BROWSERS:
        driver = get_driver(browser)
        try:
            test_logic(driver)
        finally:
            driver.quit()
