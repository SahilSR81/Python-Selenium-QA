from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys("tester")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("test31234")
driver.find_element(By.TAG_NAME,"button").click()

error = driver.find_element(By.ID, "flash")
assert "Your username is invalid" in error.text

driver.quit()
