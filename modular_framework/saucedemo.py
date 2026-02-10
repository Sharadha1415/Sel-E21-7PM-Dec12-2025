import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id', 'password').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('id', 'login-button').click()
time.sleep(3)
driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]/../../..//button[text()="Add to cart"]').click()
time.sleep(1)
driver.find_element('xpath', '//div[@id="shopping_cart_container"]').click()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Checkout"]').click()
time.sleep(2)

driver.find_element('xpath', '//input[@id="first-name"]').send_keys("Ligy")
time.sleep(1)
driver.find_element('xpath', '//input[@id="last-name"]').send_keys("John")
time.sleep(1)
driver.find_element('xpath', '//input[@id="postal-code"]').send_keys("560003")
time.sleep(1)
driver.find_element('xpath', '//input[@id="continue"]').click()
time.sleep(2)
driver.find_element('xpath', '//button[@id="finish"]').click()
time.sleep(2)
driver.find_element('xpath', '//button[text()="Back Home"]').click()
time.sleep(2)

driver.find_element('id', 'react-burger-menu-btn').click()
time.sleep(2)
driver.find_element('id', 'logout_sidebar_link').click()




































































































































