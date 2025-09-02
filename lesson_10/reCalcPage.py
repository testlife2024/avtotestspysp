from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Calculator():

    def __init__(self,driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.find_element(By.CSS_SELECTOR,'#delay').clear()


    def send_values(self, time):
        """
                    Эта функция заполняет поле со временем и отправляет выбранные значения

        """
        self._driver.find_element(By.CSS_SELECTOR,'#delay').send_keys(time)
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)').click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()
        body = self._driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning').click()

    def time(self, time):
        """
                    Эта функция проверяет корректность результатов отработки калькулятора
        """
        wait = WebDriverWait(self._driver,time)
        if (wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15'))):
            return True
        else:
            return False




