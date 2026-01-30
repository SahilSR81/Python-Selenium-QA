from utils.browser_runner import run_on_all_browsers


def delete_cookies_test(driver):
    driver.get("https://example.com")
    driver.delete_all_cookies()

    assert driver.get_cookies() == []


def test_delete_cookies():
    run_on_all_browsers(delete_cookies_test)


if __name__ == "__main__":
    test_delete_cookies()
    print("All tests passed.")
