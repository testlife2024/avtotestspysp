import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from CalcPage import Calculator

driver = webdriver.Chrome()

def test_calc_time():
    result = Calculator(driver)
    result.send_values()
    result.time()
    assert result.time() == True