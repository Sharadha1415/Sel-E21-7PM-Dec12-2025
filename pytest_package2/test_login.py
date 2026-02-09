import time

class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('pooja@12345')

