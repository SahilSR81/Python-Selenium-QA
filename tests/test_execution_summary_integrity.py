def test_basic_window_integrity(driver):
    assert driver.current_window_handle is not None
    assert len(driver.window_handles) >= 1
