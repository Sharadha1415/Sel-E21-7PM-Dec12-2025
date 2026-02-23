import time
from configparser import ConfigParser

config = ConfigParser()
config.read(r"C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\property_file\config.properties")

url = config['DEFAULT']['url']
browser = config['DEFAULT']['browser']
uname = config['DEFAULT']['username']
pwd = config['DEFAULT']['password']


from selenium import webdriver

if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'edge':
    driver = webdriver.Edge()


driver.get(url)
time.sleep(2)

driver.find_element('id', 'user-name').send_keys(uname)
time.sleep(1)
driver.find_element('id', 'password').send_keys(pwd)
time.sleep(1)
driver.find_element('id', 'login-button').click()

































































