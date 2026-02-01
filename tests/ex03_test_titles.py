def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

