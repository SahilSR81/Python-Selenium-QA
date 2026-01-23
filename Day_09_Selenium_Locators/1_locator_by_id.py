from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/login"
driver.get(url)

username = driver.find_element(By.ID,"username")
username.send_keys("sahilsr81")
print("Username entered successfully.")

time.sleep(5)
driver.quit()

# output:
# Username entered successfully.
