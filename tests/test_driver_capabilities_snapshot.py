def test_driver_capabilities(driver):
    caps = driver.capabilities
    assert "browserName" in caps
    assert "browserVersion" in caps
