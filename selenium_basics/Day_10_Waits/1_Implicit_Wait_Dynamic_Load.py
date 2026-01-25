from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.find_element(By.TAG_NAME,"button").click()

element = driver.find_element(By.ID,"finish")
print(element.text)

driver.quit()
# Output:
# Hello World!
