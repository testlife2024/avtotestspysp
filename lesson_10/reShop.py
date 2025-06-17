from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Authorization():

    def __init__(self,driver):
        """
            Эта функция авторизовывает пользователя на странице https://www.saucedemo.com/

        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()


class MainPage():
    def __init__(self,driver):
        self._driver = driver
    def add_things(self):
        """
                    Эта функция добавляет выбранные вещи в корзину

        """
        self._driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
        body = self._driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        body.send_keys(Keys.PAGE_DOWN)
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()

class CartPage():
    def __init__(self,driver):
        self._driver = driver
    def checkout(self):
        """
                    Эта функция проверяет содержимое корзины

        """
        body = self._driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        self._driver.find_element(By.CSS_SELECTOR,'#checkout').click()


class Information():
    def __init__(self,driver):
        self._driver = driver

    def input_data(self):
        """
                    Эта функция заполняет контактные данные пользователя

        """
        body = self._driver.find_element(By.TAG_NAME, 'body')
        self._driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('bebra')
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('bebrova')
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('00000')
        body.send_keys(Keys.PAGE_DOWN)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
        body.send_keys(Keys.PAGE_DOWN)
        total = self._driver.find_element(By.CSS_SELECTOR,'#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
        return total











