import time


def test_intentionally_slow():
    time.sleep(3)
    assert True
