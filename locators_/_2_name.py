'''
name    :   "name" is an attribute which is also a locator.
            So, whenever we have "name" attribute, we will go for "name" locator

            DRAWBACKS
            *   name is not unique
                Multiple elements can have same name attribute and same value
                Incase of multiple occurances, name will always consider the first occurance


'''

import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/")
# time.sleep(2)
#
# driver.find_element("name", "email").send_keys("sindhu@gmail.com")
# time.sleep(1)
# driver.find_element("name", "pass").send_keys('sindhu@123456')

##########################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# driver.find_element("name", "firstname").send_keys('Sachin')
# time.sleep(1)
# driver.find_element("name", "lastname").send_keys("Tendulkar")
# time.sleep(1)
# driver.find_element("name", "reg_email__").send_keys("sachin@gmail.com")
# time.sleep(1)
# driver.find_element("name", "reg_passwd__").send_keys("sachin@123456")

##########################################################################

## EG3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html')
## To launch the html file, we should take the path of the file and give it in place of url. The filepath should be given in raw string format
time.sleep(2)

driver.find_element("name", "fname").send_keys('Nadashree')
time.sleep(1)
driver.find_element("name", "fname").send_keys("Nivedini")

## Both the values will be filled in the first cell
## Whenever we are having multiple occurances, name locator will always consider the first occurance
## name is not unique



