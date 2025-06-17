from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR,'#ajaxButton').click()
green_text = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#content > p')))
print(green_text.text)
quit()
