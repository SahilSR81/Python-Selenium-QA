from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 


driver.get("https://the-internet.herokuapp.com/dynamic_controls")
wait = WebDriverWait(driver,10)

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[onclick="swapInput()"]')))
button.click()

print("Button become clickable and clicked")
driver.quit()

# Output:
# Button became clickable and clicked
