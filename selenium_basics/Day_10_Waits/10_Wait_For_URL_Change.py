from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("dynamic_loading"))

print("URL changed")

driver.quit()

# Output:
# URL changed
