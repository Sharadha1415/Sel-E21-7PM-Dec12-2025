'''
partial link text   :   Same as link text, instead of locating the elements using complete text,
    we can locate the elements using the partial portion of the text.
    So if we locate the elements using the partial portion of the link text, then we go for partial link text locator

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
# driver.find_element("partial link text", "Books").click()
# time.sleep(2)
# driver.find_element("partial link text", "Computers").click()
# time.sleep(2)
# driver.find_element("partial link text", "Electronics").click()
# time.sleep(2)
# driver.find_element("partial link text", "Apparel").click()

############################################################################

## EG2
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.kushals.com/")
time.sleep(2)

driver.find_element("partial link text", "Bangles").click()
time.sleep(2)
driver.find_element("partial link text", "92.5 Silver").click()
time.sleep(2)
driver.find_element("partial link text", "Wedding Store").click()











