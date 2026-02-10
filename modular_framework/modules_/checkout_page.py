import time

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self):
        self.driver.find_element('xpath', '//input[@id="first-name"]').send_keys("Ligy")
        time.sleep(1)

    def enter_lastname(self):
        self.driver.find_element('xpath', '//input[@id="last-name"]').send_keys("John")
        time.sleep(1)

    def enter_postal_code(self):
        self.driver.find_element('xpath', '//input[@id="postal-code"]').send_keys("560003")
        time.sleep(1)

    def click_continue(self):
        self.driver.find_element('xpath', '//input[@id="continue"]').click()
        time.sleep(2)

    def click_finish(self):
        self.driver.find_element('xpath', '//button[@id="finish"]').click()
        time.sleep(2)

    def back_home(self):
        self.driver.find_element('xpath', '//button[text()="Back Home"]').click()
        time.sleep(2)


















