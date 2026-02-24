# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys('Ganga')
# driver.find_element('id', 'LastName').send_keys('Shintre')
# driver.find_element('id', 'Email').send_keys('ganga@gmail.com')
# driver.find_element('id', 'Password').send_keys('ganga@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('ganga@12345')

##############################################################################


import time

from selenium import webdriver
from ddt.read_excel import reading_testdata

path = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\ddt\demo_testdata.xlsx'
data = reading_testdata(path, 'reg')

## data = {'firstname': 'Ganga', 'lastname': 'Shintre', 'email_id': 'ganga@gmail.com', 'pwd': 'ganga@12345', 'confirm_pwd': 'ganga@12345'}

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(1)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(1)
driver.find_element('id', 'gender-female').click()
driver.find_element('id', 'FirstName').send_keys(data['firstname'])
driver.find_element('id', 'LastName').send_keys(data['lastname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['pwd'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])
























