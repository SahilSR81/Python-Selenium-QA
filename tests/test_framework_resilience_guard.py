def test_refresh_and_url_integrity(driver):
    current = driver.current_url
    driver.refresh()
    assert driver.current_url == current
