from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

wait = WebDriverWait(driver,10)

username = wait.until(EC.visibility_of_element_located((By.ID,"username")))
username.clear()
username.send_keys("tomsmith")

password = driver.find_element(By.NAME,"password")
password.send_keys("SuperSecretPassword!")

login_btn = driver.find_element(By.TAG_NAME,"button")
login_btn.click()

message = wait.until(EC.visibility_of_element_located((By.ID,"flash")))
print(message.text)

driver.quit()
# Output:
# You logged into a secure area!
# ×
