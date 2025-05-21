from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR,'#password').send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR,'#login-button').click()
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt').click()
body = driver.find_element(By.TAG_NAME,'body')
body.send_keys(Keys.PAGE_DOWN)
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-onesie').click()
body.send_keys(Keys.PAGE_UP)
driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').click()
driver.find_element(By.CSS_SELECTOR,'#checkout').click()
driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('Ivan')
driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('Ivanov')
driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('000000')
body.send_keys(Keys.PAGE_DOWN)
driver.find_element(By.CSS_SELECTOR,'#continue').click()
body.send_keys(Keys.PAGE_DOWN)


def test_total():
    total = driver.find_element(By.CSS_SELECTOR,'#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
    assert total == 'Total: $58.29'
    driver.quit()

