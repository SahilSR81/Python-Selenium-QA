from selenium import webdriver


def test_example_url():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    assert "example.com" in driver.current_url

    driver.quit()


if __name__ == "__main__":
    try:
        test_example_url()
        print("ex03_assert_url.py → ALL TESTS PASSED")
    except AssertionError:
        print("ex03_assert_url.py → TEST FAILED")

