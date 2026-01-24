from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.execute_script("window.open('https://www.wikipedia.org');")
print("New tab opened")

# Output:
# New tab opened

