def test_refresh_stability_parallel(driver):
    for _ in range(3):
        driver.refresh()

    assert driver.title != ""
