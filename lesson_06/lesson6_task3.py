from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
driver.implicitly_wait(30)
element = driver.find_element(By.CSS_SELECTOR,'#award').get_attribute('src')
print(element)