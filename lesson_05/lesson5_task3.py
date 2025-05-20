from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()
field = driver.find_element(By.CSS_SELECTOR,'#content input[type=number]')
field.send_keys('Sky')
field.clear()
field.send_keys('Pro')
driver.quit()

