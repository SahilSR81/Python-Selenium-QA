from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_tab_creation_parallel(driver):
    original = driver.current_window_handle

    driver.execute_script("window.open('https://example.com');")

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 10).until(EC.title_contains("Example"))

    assert "Example" in driver.title

    driver.close()
    driver.switch_to.window(original)
