import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
def setup(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome(opts)
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome(opts)

class TestRegister:

    def test_reg(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-female').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Pooja')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('Mane')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('pooja@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('pooja@12345')
        time.sleep(2)


class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('pooja@12345')


































