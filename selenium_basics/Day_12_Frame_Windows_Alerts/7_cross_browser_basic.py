from selenium import webdriver
import time

def get_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "edge":
        return webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

browsers = ["chrome","firefox","edge"]

for b in browsers:
    driver = get_driver(b)
    driver.get("https://example.com")
    print(f"{b} launched successfully.")
    time.sleep(3)
    driver.quit()

"""
output:
chrome launched successfully.
firefox launched successfully.
edge launched successfully.

"""
