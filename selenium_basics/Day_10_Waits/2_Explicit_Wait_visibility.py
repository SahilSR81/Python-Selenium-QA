from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.CSS_SELECTOR, "div[id='start'] button").click()

wait = WebDriverWait(driver,10)
visible_element = wait.until(EC.visibility_of_element_located((By.ID,"finish")))

print(visible_element.text)
driver.quit()
# Output:
# Hello World!
