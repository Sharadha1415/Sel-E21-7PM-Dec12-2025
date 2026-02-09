'''
validation methods  :   They are used to validate the data from the web-application

'''
import time

'''
is_displayed()  :   This method will check whether the element is displayed on the page or not.
                    SYNTAX  :   web_element.is_displayed()
                    
                    Return True if the web_element is displayed
                    Return False if the web_element is not displayed

'''

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
# books_1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')       ## displayed
# print(books_1.is_displayed())           ## True
#
# books_2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')       ## not displayed
# print(books_2.is_displayed())           ## False

##################################################################################################

'''
is_enabled  :   This method checks whether the element is enabled to perform the operations or not
                SYNTAX  :   web_element.is_enabled()
                
                Returns True if the element is enabled
                Returns False if the element is disabled
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/accounts/emailsignup/")
# time.sleep(2)
#
# sign_up = driver.find_element('xpath', '//button[text()="Sign up"]')        ## element will be disabled until we enter the data
# print(sign_up.is_enabled())     ## False
#
# login_with_facebook = driver.find_element('xpath', '//button[text()="Log in with Facebook"]')       ## element is enabled
# print(login_with_facebook.is_enabled())     ## True

##################################################################################################

'''
is_selected     :       Will check if the element(checkbox, radio_btn, option) is selected or not
                        SYNTAX  :   web_element.is_selected()
                        
                        Returns True if the web_element is selected
                        Returns False if the web_element is not selected

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/register")
time.sleep(2)

male_radiobtn = driver.find_element('id', 'gender-male')
male_radiobtn.click()
time.sleep(2)

female_radiobtn = driver.find_element('id', 'gender-female')

print(male_radiobtn.is_selected())          ## True
print(female_radiobtn.is_selected())        ## False





















