from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")

iframe = driver.find_element(By.ID,"frame1")
driver.switch_to.frame(iframe)

heading = driver.find_element(By.CSS_SELECTOR,"#sampleHeading").text
assert "This is a sample page" in heading

driver.switch_to.default_content()

driver.quit()
