from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/login"
driver.get(url)

password = driver.find_element(By.NAME, "password")
password.send_keys("Sahil@1234")

print("Password entered successfully.")

time.sleep(5)
driver.quit()

# output:
# Password entered successfully.
