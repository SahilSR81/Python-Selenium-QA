def test_env_navigation(driver, env_config):
    driver.get(env_config["base_url"])
    assert driver.current_url.startswith("http")
