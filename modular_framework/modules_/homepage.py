import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()

    def add_product_to_cart(self):
        self.driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]/../../..//button[text()="Add to cart"]').click()
        time.sleep(1)

    def click_cart_icon(self):
        self.driver.find_element('xpath', '//div[@id="shopping_cart_container"]').click()
        time.sleep(2)

    def click_burger_menu(self):
        self.driver.find_element('id', 'react-burger-menu-btn').click()
        time.sleep(2)

    def click_logout(self):
        self.driver.find_element('id', 'logout_sidebar_link').click()

