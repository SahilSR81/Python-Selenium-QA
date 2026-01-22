from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

driver.refresh()
print("Page refreshed")

# Output:
# Page refreshed

