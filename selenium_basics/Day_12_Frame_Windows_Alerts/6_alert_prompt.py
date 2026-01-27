from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.find_element(By.XPATH,"//button[@id='promptexample']").click()

alert = driver.switch_to.alert
alert.send_keys("SAHIL")
alert.accept()

result = driver.find_element(By.ID,"promptreturn").text

# assert "SAHIL" in result     //true
assert "sahil" in result
"""    assert "sahil" in result
           ^^^^^^^^^^^^^^^^^
AssertionError     """

driver.switch_to.default_content()
driver.quit()
