from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "edge":
        return webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser.")

def app_flow(driver,browser):
    print(f"\nOpening in {browser}.")

    # iFrame
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()

    driver.switch_to.frame("frame1")
    msg = driver.find_element(By.CSS_SELECTOR,"#sampleHeading").text
    print(f"{browser} -> iframe text:",msg)
    driver.switch_to.default_content()

    # Alert
    driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    driver.find_element(By.XPATH, "//button[@id='alertexamples']").click()

    alert = driver.switch_to.alert
    print(f"{browser} -> alert text:",alert.text)
    alert.accept()

    # Window
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID,"tabButton").click()

    parent = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != parent:
            driver.switch_to.window(handle)
            print(f"{browser} -> new tab text:",msg)
            driver.close()

    driver.switch_to.window(parent)
    driver.quit()

browsers = ["chrome","firefox","edge","opera"]
for b in browsers:
    drv = get_driver(b)
    app_flow(drv,b)

"""
Output:
Opening in chrome.
chrome -> iframe text: This is a sample page
chrome -> alert text: I am an alert box!
chrome -> new tab text: This is a sample page

Opening in firefox.
firefox -> iframe text: This is a sample page
firefox -> alert text: I am an alert box!
firefox -> new tab text: This is a sample page

Opening in edge.
edge -> iframe text: This is a sample page
edge -> alert text: I am an alert box!
edge -> new tab text: This is a sample page
Traceback (most recent call last):
  File "/home/sahilsr81/projects/Python-Selenium-QA/selenium_basics/Day_12_Frame_Windows_Alerts/8_cross_browser_iframe.py", line 50, in <module>
    drv = get_driver(b)
  File "/home/sahilsr81/projects/Python-Selenium-QA/selenium_basics/Day_12_Frame_Windows_Alerts/8_cross_browser_iframe.py", line 12, in get_driver
    raise ValueError("Unsupported Browser.")
ValueError: Unsupported Browser.
"""
