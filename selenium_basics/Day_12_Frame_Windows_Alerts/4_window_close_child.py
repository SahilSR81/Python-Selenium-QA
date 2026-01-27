from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.ID,"windowButton").click()

parent = driver.current_window_handle

for handle in driver.window_handles:
    if handle != parent:
        driver.switch_to.window(handle)
        driver.close()

driver.switch_to.window(parent)
print(driver.title)

driver.switch_to.default_content()
driver.quit()
# output:
# This is a sample page
