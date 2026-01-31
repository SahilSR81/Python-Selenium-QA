from selenium import webdriver
from selenium.webdriver.common.by import By


def test_h1_element_present():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    heading = driver.find_element(By.TAG_NAME, "h1")

    assert heading.is_displayed()
    assert heading.text == "Example Domain"

    driver.quit()


if __name__ == "__main__":
    try:
        test_h1_element_present()
        print("ex04_element_presence.py → ALL TESTS PASSED")
    except AssertionError:
        print("ex04_element_presence.py → TEST FAILED")

