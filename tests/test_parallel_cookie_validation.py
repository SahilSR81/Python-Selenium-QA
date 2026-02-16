def test_cookie_addition_parallel(driver):
    driver.add_cookie({"name": "parallel_test", "value": "xdist"})

    cookie = driver.get_cookie("parallel_test")
    assert cookie["value"] == "xdist"
