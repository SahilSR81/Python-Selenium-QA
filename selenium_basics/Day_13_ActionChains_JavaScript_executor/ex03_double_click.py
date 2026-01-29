from utils.browser_runner import run_on_all_browsers
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def double_click_test(driver):
    driver.get("https://demoqa.com/buttons")

    btn = driver.find_element(By.ID, "doubleClickBtn")
    ActionChains(driver).double_click(btn).perform()

    msg = driver.find_element(By.ID, "doubleClickMessage")
    assert msg.is_displayed()


def test_double_click():
    run_on_all_browsers(double_click_test)

if __name__ == "__main__":
    test_double_click()
    print("All tests passed.")
