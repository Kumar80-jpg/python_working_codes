from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

#Finding Elements
element = driver.find_element(By.ID,"content")
element = driver.find_element(By.XPATH)

#wait
Wait  = WebDriverWait(driver,10)
element = Wait.until(EC.presence_of_all_elements_located(By.id,"content"))

#Interactions
element.click()
element.send_keys('folder')
element.clear()


#Screenshots
driver.save_screenshot("demo.png")