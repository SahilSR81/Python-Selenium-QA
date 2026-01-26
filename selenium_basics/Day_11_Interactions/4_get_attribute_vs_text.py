from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID,"username")
username.send_keys("testuser")

password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("Test#1234")

print("Attribute value:",username.get_attribute("value"))
print("Attribute value:", password.get_attribute("value"))

time.sleep(3)
driver.quit()

#output:
# Attribute value: testuser
# Attribute value: Test#1234