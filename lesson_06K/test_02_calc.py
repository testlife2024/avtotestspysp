from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)').click()
driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()
driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning').click()

def test_15():
    wait = WebDriverWait(driver, 45)
    assert (wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15'))) == True
    driver.quit()



