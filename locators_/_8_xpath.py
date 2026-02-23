'''
xpath   :   It is a locator to locate any element on the application uniquely.
            Using xpath, we can locate the web elements using attributes, using text, can do indexing, can locate
            dynamically changing elements.
            We can locate any element on the application using xpath

            There are 2 types of xpath
            *   Absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

                                    DRAWBACKS
                                    *   Depends on the full path from the root
                                    *   Difficult to maintain
                                    *   Not reusable
                                    *   Not readable
                                    *   Very lengthy and time consuming

            *   relative xpath  :   Doesnot start from the root of html
                                    We use // to write the relative xpath
                                    // represents any child

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
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[1]/td/input').send_keys('Faizan')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[2]/td/input').send_keys('faizan@12345')

#########################################################################################################

# ## EG2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()

#########################################################################################################

'''
        Attribute name and attribute value
        SYNTAX  :   //tagname[@attr_name="attr_value"]
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="field-keywords"]').send_keys('Perfume')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="nav-search-submit-button"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[@class="a-truncate-cut"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@data-group="men"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="genz"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG4
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.jiomart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[@id="btn_location_close_icon"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="rel_pincode"]').send_keys('560003')
# time.sleep(2)
# driver.find_element('xpath', '//button[@id="btn_pincode_submit"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@type="search"]').send_keys('Phone')
# time.sleep(1)
# driver.find_element('xpath', '//span[@class="line-clamp"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG5
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://chat.qspiders.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="username"]').send_keys('chaithra@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('chaitra@1234')
# time.sleep(1)
# driver.find_element('xpath', '//button[@type="submit"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG6

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@aria-label="Mobile Number or Email"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@type="password"]').send_keys('harry@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="fullName"]').send_keys('harry_potter')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="username"]').send_keys('harry_12345678')

#########################################################################################################

'''
        Using text
        SYNTAX  :   //tagname[text()="text"]
        
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Bestsellers"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Most Gifted"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Amazon Launchpad"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Collections"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="TVs & Appliances"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Become a Seller"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="mobileNumber"]').send_keys('9874563210')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="email"]').send_keys('cm_gowda@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="password"]').send_keys('cm@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="confirmPassword"]').send_keys('cm@12345')
# time.sleep(1)
# driver.find_element('xpath', '//span[text()="Register & Continue"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="ADD TO CART"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@class="cart-icon"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="PROCEED TO CHECKOUT"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@class="promoCode"]').send_keys('CAP1234')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Apply"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Place Order"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG4
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://x.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Create account"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[@aria-label="Close"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Sign up with Google"]').click()

##----------------------------------------------------------------------------------------------------

## EG5

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www2.hm.com/en_in/index.html')
# time.sleep(4)
#
# driver.find_element('xpath', '//a[text()="Ladies"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Home"]').click()

##----------------------------------------------------------------------------------------------------

# ## EG6
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Genz"]').click()


#########################################################################################################

'''
Group indexing  :   (any_xpath)[index_num]
If we dont give any index number, by default it will always consider the first occurance    
'''

# ## EG1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Sanchitha')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('R')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('sanchitha@gmail.com')
#
# ##----------------------------------------------------------------------------------------------------

# ## EG2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M5-Dec13-Weekend\files_\css_selector.html')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('Chaithra')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Sowmya')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Shruti')

##----------------------------------------------------------------------------------------------------

# ## EG3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[@class="desktop-main"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[5]').click()

#########################################################################################################

'''
contains    :   To locate the web-elements using the partial text of any tagname, we use contains
                SYNTAX  :   //tagname[contains(text(), "partial_text")]
'''

# ## EG1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.purplle.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[contains(text(), "BRANDS")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[contains(text(), "OFFERS")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[contains(text(), "MAGAZINE")]').click()
#
# ##----------------------------------------------------------------------------------------------------

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Men in Silver")]').click()

# ##----------------------------------------------------------------------------------------------------
#
# ## EG3
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
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Electronics")])[3]').click()

#########################################################################################################
'''
Independent - dependent xpath
    *   Identify the dependent-independent elements
    *   write the xpath of the independent element
    *   Traverse back until we get the common match for dependent-independent elements
    *   Continue writing the xpath for the dependent element
'''

'''
EG1.    wap to click on the checkbox of Ruby
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()

##----------------------------------------------------------------------------------------------------
'''
EG2.    wap to click on the download link of windows
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

##----------------------------------------------------------------------------------------------------

'''
EG3.    wap to click on the release notes of python 3.13.8 in https://www.python.org/
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Downloads"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Python 3.13.8"]/../..//a[text()="Release notes"]').click()

##----------------------------------------------------------------------------------------------------

'''
Eg4.    wap to print the buy-price and sell-price of gold in https://www.iforex.in/tools/live-rates
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(2)
#
# driver.find_element('xpath', '//div[@id="ai-chat-close"]').click()
# time.sleep(3)
#
# sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(f'The sellprice of gold is {sellprice.text}')
#
# buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f'The buyprice of gold is {buyprice.text}')

##----------------------------------------------------------------------------------------------------
'''
Eg5.    wap to print the price of MRF in https://in.tradingview.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@type="search"]').send_keys('MRF')
# time.sleep(2)
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
#
# mrf = driver.find_element('xpath', '(//span[text()="MRF"])[4]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(mrf.text)

#########################################################################################################
'''
Parent to child -->    parent//child
    
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('xpath', '//div[@class="block block-category-navigation"]//a[contains(text(), "Books")]').click()
#
# ##----------------------------------------------------------------------------------------------------
#
# ## EG2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
# driver.find_element('xpath', '//div[@id="nav-search"]//input').send_keys('mobiles')

#########################################################################################################

'''
child to parent     :   child_element/parent::tagname_of_parent
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# # driver.find_element('xpath', '//input[@name="username"]/..')        ## goes back to one parent
# # driver.find_element('xpath', '//input[@name="username"]/../..')     ## goes back twice(parent of immediate parent)

##
# driver.find_element('xpath', '//input[@name="username"]/parent::label')     ## go back to the immediate parent only

#########################################################################################################

'''
siblings    :   web_element/preceding-sibling::tagname_of_sibling_ele
                web_element/preceding-sibling::tagname_of_sibling_ele[index_num]
                
                web_element/following-sibling::tagname_of_sibling_ele
                web_element/following-sibling::tagname_of_sibling_ele[index_num]

'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/")
#
# ## preceding-sibling
# driver.find_element('xpath', '//input[@name="username"]/preceding-sibling::span')
#
# ## following-sibling
# driver.find_element('xpath', '//span[contains(text(), "Phone number")]/following-sibling::input')

#########################################################################################################

'''
ancestor    :   web_element/ancestor::tagname_of_ancestor_ele
                web_element/ancestor::tagname_of_ancestor_ele[index_num]
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Phone number")]/ancestor::div')
#
# ## Incase of multiple occurances, we can do direct indexing
# driver.find_element('xpath', '//span[contains(text(), "Phone number")]/ancestor::div[n]')


#########################################################################################################
'''
descendant  :   web_element/descendant::tagname_of_descendant_ele
                web_element/descendant::tagname_of_descendant_ele[index_num]
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.instagram.com/")
#
# ## locating the descendant elements using //
# driver.find_element('xpath', '//form[@id="loginForm"]//input[@name="username"]')
#
# ## locating the descendants using descendant xpath
# driver.find_element('xpath', '//form[@id="loginForm"]/descendant::input')
#

#########################################################################################################

'''
css selector vs xpath

*   Cannot locate text using css selector               *   Can locate text using xpath
*   Indexing is not possible                            *   Indexing is possible
*   Backtraversing is not possible                      *   Backtraversing is possible in xpath
*   Cannot locate dynamically changing elements         *   Can locate dynamically changing elements

'''


















