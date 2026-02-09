'''
Getter methods  :   Getting the data from the web-elements

'''
import time

'''
tag_name    :   This is a property.
                This gives the tagname of the web-element  
                SYNTAX  :   web_element.tag_name
'''

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
# search_bar = driver.find_element('id', 'small-searchterms')
# print(search_bar.tag_name)          ## input
#
# community_poll = driver.find_element('xpath', '//strong[text()="Community poll"]')
# print(community_poll.tag_name)      ## strong

########################################################################################

'''
text    :   It is a property.
            It will give the text of the web-element
            
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
# reg = driver.find_element('xpath', '//a[@class="ico-register"]')
# print(reg.text)
#
# login = driver.find_element('xpath', '//a[@class="ico-login"]')
# print(login.text)


########################################################################################

'''
get_attribute()     :   This method will give the attribute value
                        SYNTAX  :   web_element.get_attribute("attr_name")
'''
#
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
# reg = driver.find_element('xpath', '//a[text()="Register"]')
# print(reg.get_attribute("href"))        ## https://demowebshop.tricentis.com/register
# print(reg.get_attribute("class"))       ## ico-register
#
# login = driver.find_element('xpath', '//a[text()="Log in"]')
# print(login.get_attribute("href"))      ## https://demowebshop.tricentis.com/login
# print(login.get_attribute("class"))     ## ico-login

########################################################################################

'''
get_dom_attribute()     :   This method will give the attribute value as it is written in the html
                            SYNTAX  :   web_element.get_dom_attribute("attr_name")
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
# reg = driver.find_element('xpath', '//a[text()="Register"]')
# print(reg.get_dom_attribute("href"))        ## /register
#
# login = driver.find_element('xpath', '//a[text()="Log in"]')
# print(login.get_dom_attribute("href"))      ## /login

########################################################################################

'''
value_of_css_property   :   Fetches the css value of the web-element
                            Used to verify styles like font-size, color etc,..
'''

# ## Eg1
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
# login_link = driver.find_element('xpath', '//a[text()="Log in"]')
# print(login_link.value_of_css_property("color"))            ## rgba(175, 3, 4, 1)
# print(login_link.value_of_css_property("font-size"))        ## 12px

##-------------------------------------------------------------------------------------
#
# ## Eg2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
# driver.find_element('id', 'user-name').send_keys('Sanjay_M')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('sanjay@12345')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(2)
# error_msg_container = driver.find_element('xpath', '//div[@class="error-message-container error"]')
# print(error_msg_container.value_of_css_property("color"))

########################################################################################

'''
aria_role   :   Returns the role of a web-element
                SYNTAX  :   web_element.aria_role
'''

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
# search_bar = driver.find_element('id', 'small-searchterms')
# print(search_bar.aria_role)         ## textbox
#
# subscribe = driver.find_element('id', 'newsletter-subscribe-button')
# print(subscribe.aria_role)          ## button
#
# login = driver.find_element('xpath', '//a[text()="Log in"]')
# print(login.aria_role)              ## link

########################################################################################

'''
accessible_name :   It is a property.
                    It returns the accessible name used by the readers
'''

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
# reg = driver.find_element('class name', 'ico-register')
# print(reg.accessible_name)          ## Register
#
# search = driver.find_element('css selector', 'input[value="Search"]')
# print(search.accessible_name)       ## Search
#
# logo = driver.find_element('css selector', 'img[alt="Tricentis Demo Web Shop"]')
# print(logo.accessible_name)         ## Tricentis Demo Web Shop

########################################################################################

'''
screenshot  :   To take the screenshot of a webelement, we use screenshot()

'''

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
# # search_bar = driver.find_element("id", "small-searchterms")
# # search_bar.screenshot("searchbar.png")    ## The screenshot will be saved in the same location as our python file
#
# ## To save the screenshot in different location.
# search_bar = driver.find_element("id", "small-searchterms")
# search_bar.screenshot(r"C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\screenshots\searchbar.png")

########################################################################################

'''
get_attribute and get_dom_attribute
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

reg = driver.find_element('xpath', '//a[text()="Register"]')
print(reg.get_attribute("href"))            ## https://demowebshop.tricentis.com/register
print(reg.get_dom_attribute("href"))        ## /register




