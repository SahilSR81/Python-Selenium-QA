from utils.browser_runner import run_on_all_browsers
from selenium.webdriver.common.by import By


def js_click_test(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    btn = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    driver.execute_script("arguments[0].click()", btn)

    delete_btn = driver.find_element(By.CLASS_NAME, "added-manually")
    assert delete_btn.is_displayed()


def test_js_click():
    run_on_all_browsers(js_click_test)

if __name__ == "__main__":
    test_js_click()
    print("All tests passed.")
