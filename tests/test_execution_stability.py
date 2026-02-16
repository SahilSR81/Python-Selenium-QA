import time


def test_page_source_integrity(driver):
    time.sleep(1)
    assert len(driver.page_source) > 200


def test_window_handles_integrity(driver):
    time.sleep(1)
    assert len(driver.window_handles) >= 1
