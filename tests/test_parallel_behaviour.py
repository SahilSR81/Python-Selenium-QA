import time

def test_parallel_title_consistency(driver):
    time.sleep(1)
    assert driver.title != ""


def test_parallel_url_consistency(driver):
    time.sleep(1)
    assert driver.current_url.startswith("http")
