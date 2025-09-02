from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR,'#newButtonName').send_keys('SkyPro')
blue_button = driver.find_element(By.CSS_SELECTOR,'#updatingButton')
blue_button.click()
driver.implicitly_wait(2)
print(blue_button.text)
quit()

