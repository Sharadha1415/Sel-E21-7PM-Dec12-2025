'''
In web automation, sometimes actions open a new browser window or tab (e.g., clicking a link, pop-up, advertisement, or login window).
Selenium initially controls only the main window where the driver started.
To interact with other windows/tabs, we need to switch between them.

Window Handles
    Every window or tab opened by the browser has a unique ID, called a window handle.
    Selenium provides methods to get and switch between these handles.
    handles = driver.window_handles     ## Returns a list of handles for all open windows/tabs.

    To switch the driver to the window
    driver.switch_to.window(handles[window])

'''

import time

## EG1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

parent_handle = driver.current_window_handle

driver.find_element('xpath', '//a[text()="YouTube"]').click()
time.sleep(2)

def handle_window():
    return driver.window_handles

for handle in handle_window():
    driver.switch_to.window(handle)
    if 'youtube' in driver.current_url:
        driver.find_element('xpath', '//input[@name="search_query"]').send_keys('selenium classes')
        time.sleep(2)

driver.switch_to.window(parent_handle)
time.sleep(2)

driver.find_element('xpath', '//a[text()="Google+"]').click()
time.sleep(2)

for handle in handle_window():
    driver.switch_to.window(handle)
    if 'googleblog' in driver.current_url:
        driver.find_element('xpath', '//input[@placeholder="Search blog"]').send_keys('google pixel phones')

##################################################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

parent_handle = driver.current_window_handle        ##

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
ac.move_to_element(home).perform()          ## hovering to home
time.sleep(2)

## clicking on festive decpr
driver.find_element('xpath', '//a[text()="Festive Decor"]').click()
time.sleep(2)

## clicking on the first product
driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
time.sleep(2)

## Initializing window_handles
handles = driver.window_handles
print(handles)      ## [parent_handle, child_handle]

for handle in handles:
    driver.switch_to.window(handle)     ## switching the driver to new tab/window
    if 'nestasia' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        time.sleep(2)

## switching back to the parent_window
driver.switch_to.window(parent_handle)
time.sleep(2)

## clicking on another element
driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()     ## opens in new tab

## initialize window_handles
handles2 = driver.window_handles
print(handles2)         ## [parent_handle, child_handle, child2]

for handle in handles2:
    driver.switch_to.window(handle)
    if 'backdropon' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()











