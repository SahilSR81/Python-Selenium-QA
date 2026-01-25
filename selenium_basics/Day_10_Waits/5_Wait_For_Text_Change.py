from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.TAG_NAME,"button").click()

wait = WebDriverWait(driver,10)
wait.until(EC.text_to_be_present_in_element((By.ID,"finish"),"Hello World!"))

print("text appeared successfully")

driver.quit()
# Output:
# Text appeared successfully
