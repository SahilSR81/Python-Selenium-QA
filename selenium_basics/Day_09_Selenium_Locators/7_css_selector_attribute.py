from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("cssUser")

print("CSS selector used")

time.sleep(2)
driver.quit()

# Output:
# CSS selector used
