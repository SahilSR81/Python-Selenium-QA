from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("sahilsr81")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Pass@1234")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

print("Login flow executed")

time.sleep(3)
driver.quit()

# Output:
# Login flow executed
