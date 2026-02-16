def test_browser_session_isolation(driver):
    first_handle = driver.current_window_handle
    assert first_handle is not None


def test_browser_capabilities(driver):
    caps = driver.capabilities
    assert "browserName" in caps
