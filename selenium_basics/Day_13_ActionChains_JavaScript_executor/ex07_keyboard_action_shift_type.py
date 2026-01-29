from utils.browser_runner import run_on_all_browsers
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.wait_utils import wait_visible


def keyboard_test(driver):
    driver.get("https://the-internet.herokuapp.com/key_presses")

    input_box = wait_visible(driver, (By.ID, "target"))

    ActionChains(driver).send_keys(Keys.SHIFT).perform()

    result = wait_visible(driver, (By.ID, "result"))
    assert "SHIFT" in result.text, f"Unexpected result text: {result.text}"


def test_keyboard():
    run_on_all_browsers(keyboard_test)


if __name__ == "__main__":
    test_keyboard()
    print("All tests passed.")
