def test_report_environment_capture(driver):
    assert driver.capabilities["browserName"] in ["chrome", "firefox", "MicrosoftEdge"]
