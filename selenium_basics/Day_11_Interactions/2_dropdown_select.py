from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#dropdown"))

dropdown.select_by_value("1")
time.sleep(3)
print("Selected Option 1 by value")

dropdown.select_by_index(2)
time.sleep(3)
print("Selected Option 2 by index")

driver.quit
# output:
# Selected Option 1 by value 
# Selected Option 2 by index
