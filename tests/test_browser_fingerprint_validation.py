def test_user_agent_presence(driver):
    ua = driver.execute_script("return navigator.userAgent;")
    assert ua is not None
    assert len(ua) > 10
