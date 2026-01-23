from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div[1]/div/input")
username.send_keys("test")
print("Entered using absolute xpath.")

time.sleep(10)
driver.quit()

# output:
# Entered using absolute xpath.
