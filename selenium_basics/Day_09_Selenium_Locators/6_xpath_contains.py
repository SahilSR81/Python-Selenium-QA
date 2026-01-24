from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

login_button = driver.find_element(By.XPATH,"//button[contains(@class,'radius')]")
login_button.click()

print("Clicked login button using contains()")

time.sleep(5)
driver.quit()

# output:
# Clicked login button using contains()
