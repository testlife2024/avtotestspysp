import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Shop import *
driver = webdriver.Firefox()
def test():
    step1= Authorization(driver)
    step2 = MainPage(driver).add_things()
    step3 = CartPage(driver).checkout()
    step4 = Information(driver).input_data()
    driver.quit()
    assert step4 == 'Total: $58.29'