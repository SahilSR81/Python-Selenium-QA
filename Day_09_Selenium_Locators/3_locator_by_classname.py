from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
#driver = webdriver.Chrome() for cchrome browser
url = "https://the-internet.herokuapp.com/login"
driver.get(url)

login_button = driver.find_element(By.CLASS_NAME,"radius")
login_button.click()
print("login button clicked.")

time.sleep(4)
driver.quit()

#output:
#login button clicked.