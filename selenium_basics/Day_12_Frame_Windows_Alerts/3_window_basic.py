from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.ID, "tabButton").click()

handles = driver.window_handles
driver.switch_to.window(handles[1])

print(driver.find_element(By.CSS_SELECTOR,"#sampleHeading").text)

driver.switch_to.default_content()
driver.quit()
# output: 
# This is a sample page
