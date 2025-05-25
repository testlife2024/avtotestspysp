import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_red_field(driver):
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > label > input').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2) > label > input').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div.col-md-4.py-2 > label > input').send_keys(
        'Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(3) > label > input').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(1) > label > input').send_keys(
        'test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(2) > label > input').send_keys(
        '+7985899998787')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div.col-md-2.py-2 > label > input').send_keys('')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(4) > label > input').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div:nth-child(1) > label > input').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div:nth-child(2) > label > input').send_keys('SkyPro')

    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'button').click()
    assert driver.find_element(By.CSS_SELECTOR,'#zip-code').get_attribute('class') == 'alert py-2 alert-danger'


def test_green_field(driver):
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > label > input').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2) > label > input').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div.col-md-4.py-2 > label > input').send_keys(
        'Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(3) > label > input').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(1) > label > input').send_keys(
        'test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(2) > label > input').send_keys(
        '+7985899998787')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div.col-md-2.py-2 > label > input').send_keys('')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(4) > label > input').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div:nth-child(1) > label > input').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div:nth-child(2) > label > input').send_keys('SkyPro')

    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, 'button').click()
    el1 = driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute('class')
    el2 = driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute('class')
    el3 = driver.find_element(By.CSS_SELECTOR, '#address').get_attribute('class')
    el4 = driver.find_element(By.CSS_SELECTOR, '#city').get_attribute('class')
    el5 = driver.find_element(By.CSS_SELECTOR, '#country').get_attribute('class')
    el6 = driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute('class')
    el7 = driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute('class')
    el8 = driver.find_element(By.CSS_SELECTOR, '#job-position').get_attribute('class')
    el9 = driver.find_element(By.CSS_SELECTOR, '#company').get_attribute('class')
    green_fields = [el2,el4,el9,el8,el7,el3,el5,el6,el1]
    assert set(green_fields) == {'alert py-2 alert-success'}






