import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys('Sanchitha')
# driver.find_element('id', 'LastName').send_keys('Ramesh')
# driver.find_element('id', 'Email').send_keys('sanchitha@gmail.com')
# driver.find_element('id', 'Password').send_keys('sanchitha@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('sanchitha@12345')


##############################################################################################

import time
from read_excel import read_test_data

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

data = read_test_data("reg")
## {'fname': 'Sanchitha', 'lname': 'Ramesh', 'email_id': 'sanchitha@gmail.com', 'pwd': 'sanchitha@12345', 'confirm_pwd': 'sanchitha@12345'}


driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('id', 'gender-female').click()
driver.find_element('id', 'FirstName').send_keys(data['fname'])
driver.find_element('id', 'LastName').send_keys(data['lname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['pwd'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])


































