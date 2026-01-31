from selenium import webdriver


def test_example_title():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    assert driver.title == "Example Domain"

    driver.quit()


if __name__ == "__main__":
    try:
        test_example_title()
        print("ex02_assert_title.py → ALL TESTS PASSED")
    except AssertionError:
        print("ex02_assert_title.py → TEST FAILED")

