from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.TAG_NAME, "button").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.ID, "loading")))

print("Loader disappeared")

driver.quit()
# Output:
# Loader disappeared
