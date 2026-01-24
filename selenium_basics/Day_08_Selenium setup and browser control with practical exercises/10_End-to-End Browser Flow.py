from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

print("Title:", driver.title)

driver.quit()
print("Browser session ended")

# Output:
# Title: Google
# Browser session ended

