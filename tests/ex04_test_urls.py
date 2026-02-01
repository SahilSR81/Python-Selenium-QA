def test_current_url(driver):
    driver.get("https://example.com")
    assert driver.current_url.startswith("https")

