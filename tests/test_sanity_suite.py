import pytest


@pytest.mark.sanity
def test_window_handle_exists(driver):
    assert len(driver.window_handles) >= 1


@pytest.mark.sanity
def test_browser_name(driver):
    assert driver.capabilities["browserName"] in ["chrome", "firefox", "MicrosoftEdge"]
