from utils.browser_runner import run_on_all_browsers


def get_cookies_test(driver):
    driver.get("https://example.com")

    cookies = driver.get_cookies()
    assert cookies is not None

    for cookie in cookies:
        print(cookie)


def test_get_cookies():
    run_on_all_browsers(get_cookies_test)


if __name__ == "__main__":
    test_get_cookies()
    print("All tests passed.")
