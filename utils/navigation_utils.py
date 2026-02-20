def open_url(driver, url):
    driver.get(url)


def refresh_page(driver):
    driver.refresh()


def get_current_url(driver):
    return driver.current_url
