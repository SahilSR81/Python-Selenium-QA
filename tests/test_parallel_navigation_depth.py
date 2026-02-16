import time


def test_multiple_navigation_cycles(driver):
    urls = [
        "https://the-internet.herokuapp.com/",
        "https://the-internet.herokuapp.com/login",
    ]

    for url in urls:
        driver.get(url)
        time.sleep(0.5)
        assert "The Internet" in driver.title or "Login" in driver.title
