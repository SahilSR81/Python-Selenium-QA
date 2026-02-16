import time

def test_runtime_measurement(driver):
    start = time.time()
    assert driver.title != ""
    duration = round(time.time() - start, 4)

    print(f"\nExecution duration: {duration} seconds")
    assert duration >= 0
