from utils.browser_runner import run_on_all_browsers
from utils.wait_utils import wait_visible
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def hover_test(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")

    avatar = wait_visible(driver, (By.CLASS_NAME, "figure"))
    ActionChains(driver).move_to_element(avatar).perform()

    caption = wait_visible(driver, (By.CLASS_NAME, "figcaption"))
    assert caption.is_displayed(), "Caption not visible after hover"


def test_hover():
    run_on_all_browsers(hover_test)

if __name__ == "__main__":
    test_hover()
    print("All tests passed.")
