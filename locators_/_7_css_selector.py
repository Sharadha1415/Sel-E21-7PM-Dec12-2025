'''
css selector    :   To locate the web-elements using any attribute, we go for css selector
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Indexing is not possible.
                        Whenever there are multiple occurances, css selector will always consider the first occurancee
                    *   Cannot locate text using css selector
                    *   Back traversing is not possible.

'''

import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# driver.find_element("css selector", 'input[placeholder="Username"]').send_keys("standard_user")
# time.sleep(1)
# driver.find_element("css selector", 'input[placeholder="Password"]').send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element("css selector", 'input[id="login-button"]').click()
# time.sleep(2)

#####################################################################################################

# ## EG2
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
# driver.find_element('css selector', 'input[name="firstname"]').send_keys('Sanjay')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="lastname"]').send_keys('M')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('sanjay@gmail.com')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('sanjay@12345')

#####################################################################################################

## EG3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'input[id="gender-male"]').click()
# driver.find_element('css selector', 'input[id="FirstName"]').send_keys('Surya')
# driver.find_element('css selector', 'input[id="LastName"]').send_keys('Narayan')
# driver.find_element('css selector', 'input[id="Email"]').send_keys('surya@gmail.com')
# driver.find_element('css selector', 'input[id="Password"]').send_keys('surya@12345')
# driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys('surya@12345')
#

#####################################################################################################
## EG4
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)

driver.find_element('css selector', 'input[type="text"]').send_keys('Nandini')
time.sleep(1)
driver.find_element('css selector', 'input[type="text"]').send_keys('YR')





















