def test_parallel_worker_visible(driver):
    assert driver.current_window_handle is not None
