from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()

wait = WebDriverWait(driver,10)
wait.until(EC.alert_is_present())

alert = driver.switch_to.alert
alert.accept()

print("alert accepted")

driver.quit()
# Output:
# Alert accepted
