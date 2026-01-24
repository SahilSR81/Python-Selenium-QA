#works only after successful login
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

msg = driver.find_element(By.ID, "flash").text
print(msg)

time.sleep(2)
driver.quit()

# Output:
# You logged into a secure area!
