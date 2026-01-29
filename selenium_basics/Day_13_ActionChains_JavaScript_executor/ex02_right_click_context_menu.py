from utils.browser_runner import run_on_all_browsers
from utils.wait_utils import wait_visible
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def right_click_test(driver):
    driver.get("https://the-internet.herokuapp.com/context_menu")

    box = wait_visible(driver, (By.ID, "hot-spot"))
    ActionChains(driver).context_click(box).perform()

    alert = driver.switch_to.alert
    assert "You selected" in alert.text
    alert.accept()

def test_context_menu():
    run_on_all_browsers(right_click_test)

if __name__ == "__main__":
    test_context_menu()
    print("All tests passed.")
