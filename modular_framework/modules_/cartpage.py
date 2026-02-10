import time

class CartPage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()

    def click_checkout(self):
        self.driver.find_element('xpath', '//button[text()="Checkout"]').click()
        time.sleep(2)


































































