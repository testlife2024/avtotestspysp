import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from reCalcPage import Calculator
from reShop import *


driver1 = webdriver.Chrome()
driver2 = webdriver.Firefox()



@allure.title('Оформление заказа')
@allure.description('Итоговая цена должна соответствовать сумме товаров')
@allure.severity(Severity.CRITICAL)
def test():
    with allure.step('Авторизация пользователя'):
        step1 = Authorization(driver2)
    with allure.step('Добавление вещей в корзину'):
        step2 = MainPage(driver2).add_things()
    with allure.step('Проверка содержимого корзины'):
        step3 = CartPage(driver2).checkout()
    with allure.step('Заполнение контактной информации для заказа'):
        step4 = Information(driver2).input_data()
    driver2.quit()
    assert step4 == 'Total: $58.29'


@allure.title('Работа калькулятора')
@allure.description('Введенное в поле Время значение должно соответствовать времени подсчета Калькулятора')
@allure.severity(Severity.BLOCKER)
def test_calc_time():
    with allure.step('Переход в калькулятор'):
        result = Calculator(driver1)
    with allure.step('Заполнение значений (время / слагаемые'):
        result.send_values(45)
        result.time(45)
    assert result.time(45) == True