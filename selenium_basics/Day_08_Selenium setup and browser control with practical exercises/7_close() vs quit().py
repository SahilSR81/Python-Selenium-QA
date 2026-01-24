from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.close()   # closes current browser window
# driver.quit()  # closes all browser windows and ends session

print("Browser close executed")

# Output:
# Browser close executed

