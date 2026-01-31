from selenium import webdriver
from selenium.webdriver.common.by import By


def test_example_page_validations():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Title & URL validation
    assert driver.title == "Example Domain"
    assert "example.com" in driver.current_url

    # Element validations
    h1 = driver.find_element(By.TAG_NAME, "h1")
    paragraph = driver.find_element(By.TAG_NAME, "p")

    assert h1.text == "Example Domain"
    assert len(paragraph.text) > 20

    driver.quit()


if __name__ == "__main__":
    try:
        test_example_page_validations()
        print("ex05_multiple_asserts.py → ALL TESTS PASSED")
    except AssertionError:
        print("ex05_multiple_asserts.py → TEST FAILED")

