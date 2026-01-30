from utils.browser_runner import run_on_all_browsers


def add_cookie_test(driver):
    driver.get("https://example.com")

    driver.add_cookie({"name": "qa_session", "value": "automation"})

    cookies = driver.get_cookies()
    assert any(c["name"] == "qa_session" for c in cookies)


def test_add_cookie():
    run_on_all_browsers(add_cookie_test)


if __name__ == "__main__":
    test_add_cookie()
    print("All tests passed.")
