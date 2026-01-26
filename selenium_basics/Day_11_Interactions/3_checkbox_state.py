from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

time.sleep(5)
print("All checkboxes selected")

driver.quit()
# output:
# All checkboxes Selected
