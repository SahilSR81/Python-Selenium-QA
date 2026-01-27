from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")

iframe = driver.find_element(By.ID,"frame1")
driver.switch_to.frame(iframe)

text = driver.find_element(By.ID,"sampleHeading").text
print(text)

driver.switch_to.default_content()
driver.quit()
# output:
# This is a sample page
