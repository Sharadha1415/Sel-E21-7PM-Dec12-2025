'''
SYNCHRONIZATION :   Matching the speed of the webdriver to the web-application
    *   The automation script will execute very fast, but the application might be slow.
    *   Web-elements might take some extra time to get loaded, so when the element is not loaded, we get error

    To avoid the error, we will make the automation script wait until the element is available

    If we don't handle them, we might get
        *   NoSuchElementException
        *   TimeOutException

    To handle the application smoothly, we make use of synchronization process

    There are 2 types of synchronization
    *   unconditional synchronization   :   No conditions are passed
            We achieve unconditional synchronization by passing time.sleep()
            This is a static wait
            It will wait for the specific amount of time given and only after the sleep time is completed, it will perform the operation.
            This process is not efficient as unnecessary wait is too much here

    *   conditional synchronization     :   Conditions are passed
            There are 2 types
            *   implicit_wait   :   Conditions are internally taken
                    SYNTAX      :   driver.implicitly_wait(n)
                                    The script will wait only until the element is available, as soon as the element is available, it will start performing the operations right away.
                                    There is no unnecessary wait
                                    A single implicit_wait is sufficient for the whole program. It will apply globally for all the elements

            *   explicit_wait   :   Conditions are externally given.
                    We have to import WebDriverWait and expected_conditions

                    from selenium import webdriver
                    from selenium.webdriver.support.ui import WebDriverWait
                    from selenium.webdriver.support import expected_conditions as EC

                    opts = webdriver.ChromeOptions()
                    opts.add_experimental_option("detach", True)

                    driver = webdriver.Chrome(opts)

                    wait_obj = WebDriverWait(driver, 30)

                    wait_obj.until(EC.condition)

                It will wait until the condition is satisfied and then it will go to the next line
                If the condition is not satisfied, then it will give TimeOutException

'''

import time

# ## time.sleep()
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\loading.html')
# time.sleep(20)
#
# driver.find_element("name", "fname").send_keys("Ligy")
# time.sleep(1)
# driver.find_element("name", "lname").send_keys("John")


###################################################################################################

'''
implicit_wait
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\loading.html')
#
# driver.find_element("name", "fname").send_keys("Ligy")
# time.sleep(1)
# driver.find_element("name", "lname").send_keys("John")


###################################################################################################

'''
explicitly_wait
'''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\loading.html')
#
# wait_obj.until(EC.visibility_of_element_located(("xpath", '//div[contains(text(), "FirstName")]')))
#
# driver.find_element("name", "fname").send_keys("Ligy")
# time.sleep(1)
# driver.find_element("name", "lname").send_keys("John")

# ###################################################################################################
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait = WebDriverWait(driver, 10)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# driver.find_element("id", "user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element("id", "password").send_keys("secret_sauceeee")
# time.sleep(1)
# driver.find_element("id", "login-button").click()
#
# try:
#     wait.until(expected_conditions.url_contains("inventory"))
#     print("successfull login")
# except:
#     print("unsuccessfull login")

###################################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element("id", "user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element("id", "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element("id", "login-button").click()

try:
    wait.until(expected_conditions.visibility_of_element_located(("xpath", '//span[text()="Products"]')))
    print("successfull login")
except:
    print("unsuccessfull login")

# ###################################################################################################
#
#
# ## time.sleep()
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element("xpath", '//button[text()="Click Me"]').click()
# time.sleep(50)
# driver.find_element("xpath", '//button[text()="Click Me"]').click()


###################################################################################################

# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(50)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element("xpath", '//button[text()="Click Me"]').click()
# driver.find_element("xpath", '//div[text()="100%"]')
# time.sleep(2)
# driver.find_element("xpath", '//button[text()="Click Me"]').click()

###################################################################################################

## explicit_wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait = WebDriverWait(driver, 50)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\progressbar.html')
time.sleep(2)

driver.find_element("xpath", '//button[text()="Click Me"]').click()
wait.until(EC.visibility_of_element_located(("xpath", '//div[text()="100%"]')))
time.sleep(2)
driver.find_element("xpath", '//button[text()="Click Me"]').click()



















