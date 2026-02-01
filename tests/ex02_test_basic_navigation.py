def test_open_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title

