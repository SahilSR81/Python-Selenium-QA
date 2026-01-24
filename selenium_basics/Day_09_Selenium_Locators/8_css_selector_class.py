from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

print("Clicked using CSS class")

time.sleep(2)
driver.quit()

# Output:
# Clicked using CSS class
