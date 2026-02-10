import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> driver = webdriver.Chrome()

    def enter_username(self):
        self.driver.find_element('id', 'user-name').send_keys('standard_user')
        time.sleep(1)

    def enter_password(self):
        self.driver.find_element('id', 'password').send_keys('secret_sauce')
        time.sleep(1)

    def click_login_btn(self):
        self.driver.find_element('id', 'login-button').click()
        time.sleep(3)
























