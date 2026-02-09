'''
class name  :   If we have "class" attribute, we can go for "class name" locator

                DRAWBACKS
                *   class is not unique.
                    We can have multiple web-elements with the same class attribute and the value.
                    Incase of multiple occurances, "class name" locator will always consider the first occurance

                *   class name locator cannot recognize the spaces
                    If there are spaces in the value of the class attribute, we should replace the space with dot(.)


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
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element("class name", "ico-register").click()
# time.sleep(2)
# driver.find_element("class name", "ico-login").click()
# time.sleep(2)
# driver.find_element("class name", "ico-cart").click()

#################################################################################

# ## EG2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html')
# time.sleep(2)
#
# driver.find_element("class name", "first_row").send_keys('Dhiraj')
# time.sleep(1)
# driver.find_element("class name", "first_row").send_keys("Faizan")
#
# ## Both the values will be filled in the first cell
# ## Whenever we are having multiple occurances, class name locator will always consider the first occurance
# ## class name is not unique

#################################################################################

# ## EG3
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element("class name", "inputtext _58mg _5dba _2ph-").send_keys('Sindhu')
#
# ## NoSuchElementException
# ## Because, the class name value is having spaces in it.
# ## class name cannot identify the spaces

##---------------------------------------------------------------------------------------------

## To overcome the above issue, we will replace the space with dot(.)

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element("class name", "inputtext._58mg._5dba._2ph-").send_keys('Sindhu')
















































