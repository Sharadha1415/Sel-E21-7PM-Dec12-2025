'''
tag name    :   We can locate the web-elements using tagname locator.
                But, tagname is not unique.
                tagname will consider only the first occurance

'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html')
time.sleep(2)

driver.find_element("tag name", "input").send_keys("Sanjay")
time.sleep(1)
driver.find_element("tag name", "input").send_keys("Faizan")














