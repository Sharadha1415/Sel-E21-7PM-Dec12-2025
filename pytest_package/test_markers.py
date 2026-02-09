'''
Markers :   To group the testcases, we use markers

There are 2 types markers
    *   inbuilt markers :   There are 4 types of inbuilt marker
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail
    *   custom markers

'''

import pytest


# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_signup    signup executing        PASSED
# ## test_markers.py::test_reg       reg executing           PASSED

###################################################################################################
#
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"                --> test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               --> test_login and test_reg will execute
# ## pytest test_markers.py -vs -m="regression"           --> test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     --> 0

###################################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

## In terminal
## pytest test_markers.py -vs -m="smoke"                --> test_login, test_signup and test_logout will execute
## pytest test_markers.py -vs -m="sanity"               --> test_login and test_reg will execute
## pytest test_markers.py -vs -m="regression"           --> test_signup and test_logout will execute
## pytest test_markers.py -vs -m="smoke and sanity"     --> test_login will execute
## pytest test_markers.py -vs -m="smoke and regression" --> test_signup and test_logout will execute
## pytest test_markers.py -vs -m="sanity and regression"--> 0
## pytest test_markers.py -vs -m="smoke or sanity"      --> All 4 will execute
## pytest test_markers.py -vs -m="sanity or regression" --> All 4 will execute
## pytest test_markers.py -vs -m="smoke or regression"  --> test_login, test_signup and test_logout will execute
## pytest test_markers.py -vs -m="not smoke"            --> test_reg will execute
## pytest test_markers.py -vs -m="not sanity"           --> test_signup and test_logout will execute
## pytest test_markers.py -vs -m="not regression"       --> test_login and test_reg will execute


###################################################################################################


# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## All the attributes of the TestSample class belongs to sanity

###################################################################################

# class TestSample:
#
#     @pytest.mark.sanity
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     @pytest.mark.sanity
#     def test_logout(self):
#         print("logout executing")

###################################################################################################

'''
skip    :   To skip the execution of the testcases, we use skip marker
            It is an unconditional skip. To skip the testcases we dont have to pass any reason or condition.
            Reason is optional parameter.
            It will skip the testcases which are decorated with @pytest.mark.skip
            
            SYNTAX  :   @pytest.mark.skip
                        def test_case():
                            pass 
'''

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")
#
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing         PASSED
# ## test_markers.py::test_signup    signup executin         PASSED
# ## test_markers.py::test_reg       reg executing           PASSED
# ## test_markers.py::test_logout                            SKIPPED (unconditional skip)

##-------------------------------------------------------------------

# @pytest.mark.skip
# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="logout is already completed")
# def test_logout():
#     print("logout executing")
#
#
# ## collected 2 items
# ## test_markers.py::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::test_logout    SKIPPED (logout is already completed)


##-------------------------------------------------------------------

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_logout(self):
#         print("logout executing")
#
#
# ## collected 2 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)


##-------------------------------------------------------------------

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.skip
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_markers.py::TestSample::test_login     login executing     PASSED
# ## test_markers.py::TestSample::test_logout                        SKIPPED (unconditional skip)


###################################################################################################

'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 
            
'''

# @pytest.mark.skipif(10%2==0, reason="tc1 already executed")
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         SKIPPED (tc1 already executed)

##-------------------------------------------------------------------

# @pytest.mark.skipif(10%2==1, reason="tc1 already executed")
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         tc1 executing       PASSED

##-------------------------------------------------------------------

# @pytest.mark.skipif(10%2==1)
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         ERROR
#
# ## Error evaluating 'skipif': you need to specify reason=STRING when using booleans as conditions.

'''
If we dont specify the reason when we use skipif, pytest will give ERROR.
reason is the mandatory parameter
'''

##-------------------------------------------------------------------

# @pytest.mark.skipif(reason="tc1 already executed")
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         SKIPPED (tc1 already executed)

'''
If we dont pass the condition, by default the condition will be considered as True
'''

##-------------------------------------------------------------------

# @pytest.mark.skipif(True, reason="already executed")
# class TestSample:
#
#     def test_case1(self):
#         print("tc1 executing")
#
#     def test_case2(self):
#         print("tc2 executing")
#
# ## collected 2 items
# ## test_markers.py::TestSample::test_case1     SKIPPED (already executed)
# ## test_markers.py::TestSample::test_case2     SKIPPED (already executed)

##-------------------------------------------------------------------

# @pytest.mark.skipif(False, reason="already executed")
# class TestSample:
#
#     def test_case1(self):
#         print("tc1 executing")
#
#     def test_case2(self):
#         print("tc2 executing")
#
# ## collected 2 items
# ## test_markers.py::TestSample::test_case1     tc1 executing       PASSED
# ## test_markers.py::TestSample::test_case2     tc2 executing       PASSED

###################################################################################################

'''
parametrize :   
'''

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]        30          PASSED


##-------------------------------------------------------------------------

# @pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (-10, 90), (9, 10), (-6, -8), (10, -10)])
# def test_add(a, b):
#     print(a + b)

'''
a, b --> (10, 20)   --> a=10, b=20
a, b --> (1, 2)     --> a=1, b=2
a, b --> (-10, 90)  --> a=-10, b=90
a, b --> (9, 10)    --> a=9, b=10
a, b --> (-6, -8)   --> a=-6, b=-8
a, b --> (10, -10)  --> a=10, b=-10   
'''

## collected 6 items
## test_markers.py::test_add[10-20]    30      PASSED
## test_markers.py::test_add[1-2]      3       PASSED
## test_markers.py::test_add[-10-90]   80      PASSED
## test_markers.py::test_add[9-10]     19      PASSED
## test_markers.py::test_add[-6--8]    -14     PASSED
## test_markers.py::test_add[10--10]   0       PASSED


##-------------------------------------------------------------------------

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b, c):
#     print(a + b + c)
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]        ERROR

##-------------------------------------------------------------------------

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait = WebDriverWait(driver, 5)

@pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('abcdefgh', '12345678')])
def test_login(username, password):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element("id", "user-name").send_keys(username)
    time.sleep(1)
    driver.find_element("id", "password").send_keys(password)
    time.sleep(1)
    driver.find_element("id", "login-button").click()

    try:
        wait.until(expected_conditions.url_contains("inventory"))
        print("successfull login")
    except:
        print("unsuccessfull login")

###################################################################################################
'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''


# @pytest.mark.xfail
# def test_rcb():
#     raise Exception
#
# ## collected 1 item
# ## test_markers.py::test_rcb       XFAIL

##-------------------------------------------------------
#
# @pytest.mark.xfail
# def test_rcb():
#     print("rcb executing")
#
# ## collected 1 item
# ## test_markers.py::test_rcb   rcb executing           XPASS
































