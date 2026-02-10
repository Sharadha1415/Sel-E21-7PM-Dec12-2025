import time

from selenium import webdriver
from modular_framework.modules_.loginpage import LoginPage
from modular_framework.modules_.homepage import HomePage
from modular_framework.modules_.cartpage import CartPage
from modular_framework.modules_.checkout_page import CheckOutPage

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

def test_product1():
    lp = LoginPage(driver)
    hp = HomePage(driver)
    cart_ = CartPage(driver)
    cp = CheckOutPage(driver)

    lp.enter_username()
    lp.enter_password()
    lp.click_login_btn()
    hp.add_product_to_cart()
    hp.click_cart_icon()
    cart_.click_checkout()
    cp.enter_firstname()
    cp.enter_lastname()
    cp.enter_postal_code()
    cp.click_continue()
    cp.click_finish()
    cp.back_home()
    hp.click_burger_menu()
    hp.click_logout()

























































































