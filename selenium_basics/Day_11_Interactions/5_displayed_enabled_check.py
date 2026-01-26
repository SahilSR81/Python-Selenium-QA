from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")

print("Displayed:", login_btn.is_displayed())
print("Enabled:", login_btn.is_enabled())

driver.quit()
# output: 
# Displayed: True
# Enabled: True
