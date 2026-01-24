from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(3)
print("Wait completed")

# Output:
# Wait completed

