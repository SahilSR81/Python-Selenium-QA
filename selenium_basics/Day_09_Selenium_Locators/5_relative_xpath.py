from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.XPATH,"//input[@id='username']")
username.send_keys("Sahil Singh")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("Pass@1234")

print("Relative Xpath used")

time.sleep(5)
driver.quit()


# output:
# Relative Xpath used
