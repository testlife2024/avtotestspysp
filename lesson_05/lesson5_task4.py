from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
username = driver.find_element(By.CSS_SELECTOR,'#username')
username.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR,'#login > button > i').click()
print(driver.find_element(By.ID,'flash').text)
quit()


