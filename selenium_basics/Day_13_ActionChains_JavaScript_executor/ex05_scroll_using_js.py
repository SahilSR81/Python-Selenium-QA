from utils.browser_runner import run_on_all_browsers
from selenium.webdriver.support.ui import WebDriverWait


def js_scroll_test(driver):
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")

    initial_height = driver.execute_script("return document.body.scrollHeight")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.body.scrollHeight") > initial_height
    )

    final_height = driver.execute_script("return document.body.scrollHeight")

    assert final_height > initial_height, "Page did not scroll/load new content"


def test_js_scroll():
    run_on_all_browsers(js_scroll_test)


if __name__ == "__main__":
    test_js_scroll()
    print("All tests passed.")
