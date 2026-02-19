import time


def test_page_load_time_threshold(driver):
    start = time.time()
    driver.refresh()
    end = time.time()

    load_time = end - start
    assert load_time < 5
