'''
assert  :   It is a keyword.
            It is used to validate the expected output with the actual output.
            assert will take a condition

            SYNTAX  :   assert condition

            If the condition is True, the test case passes and the execution will continue
            If the condition is False, then it will always give AssertionError
'''

import time

# assert 10%2==0
# print("hello world")

##------------------------------------------------------------------

# assert 11%2==0
# print("hello world")
#
# ## AssertionError

##------------------------------------------------------------------

# a = 10
#
# assert a>5, f"{a} is not greater than 5"        ## assert a>5   --> assert 10>5 --> assert True --> True
#
# ## condition is True, the execution will continue

##------------------------------------------------------------------

'''
assert not condition
'''

# a = 10
#
# assert not a>5, f"{a} is not greater than 5"
# ## assert not 10>5 --> assert not True -->  assert False --> AssertionError
#
# ## OUTPUT   -->     AssertionError
#

##------------------------------------------------------------------
'''
assert actual == expected
'''

# actual = 10
# expected = 10
#
# assert actual==expected         ## assert 10==10 --> True

##------------------------------------------------------------------
'''
assert actual != expected
'''

# actual = 10
# expected = 10
#
# assert actual!=expected         ## assert 10 != 10  --> assert False --> AssertionError
#
# ## OUTPUT   -->     AssertionError


##------------------------------------------------------------------

'''
assert value is None
'''

# assert None
#
# ## AssertionError

##------------------------------------------------------------------
'''
assert value is not None
'''
# assert not None

######################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

##--------------------------------------------------------------------
# ele1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')
# assert ele1.is_displayed()      ## True
# print("ele is displayed")

##--------------------------------------------------------------------
# ele2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')
# assert ele2.is_displayed()      ## assert False --> AssertionError

# ##--------------------------------------------------------------------
#
# expected_title = 'Demo'
# actual_title = driver.title
#
# assert expected_title == actual_title           ## AssertionError

##--------------------------------------------------------------------

# expected_title = 'Demo Web Shop'
# actual_title = driver.title
#
# assert expected_title == actual_title



































































