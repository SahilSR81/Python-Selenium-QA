from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.find_element(By.CSS_SELECTOR, "#alertexamples").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.switch_to.default_content()
driver.quit()
#output:
#I am an alert box!