from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.TAG_NAME, "button").click()

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.find_element(By.ID, "finish").is_displayed())

print("Custom wait satisfied")

driver.quit()
# Output:
# Custom wait satisfied
