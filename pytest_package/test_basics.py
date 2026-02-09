''' PYTEST  '''
import time

# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()         ## login executing
# logout()        ## logout executing
#
# ## We have to give the function call

#######################################################################################################

# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s_obj = Sample()
# s_obj.login()           ## login executing
# s_obj.logout()          ## logout executing

## To execute the methods of the class, we should create the object and call the methods


#######################################################################################################

'''
Pytest  :   It is a unit testing framework 
            Testing the small portion of the entire program, we call it as unit testing
            To perform unit testing in selenium, we use "pytest"
            
            To install pytest
            Go to command prompt    -->     pip install pytest
            
            RULES
            *   The filename should always start with test_ or end with _test
                Eg  :   test_filename.py        OR      filename_test.py
            *   Function name/method name should always start with test_
                Eg  :   def test_funcname():
                            pass 
            *   Class name should start with Test
                Eg  :   class TestClassName:
                            pass 
            
            When we follow the rules, pytest will automatically recognize the files, functions and classes which are following the rules.
            So, without giving the function call we can execute the test_function and
            without creating the object, we can execute the TestClass
            
            
            To execute the test file
            Right click anywhere on the test_file --> open in --> terminal --> test_filename.py -vs
                -v  --> Verbosity.  This gives the detailed explanation of the code
                -s  --> Scripting.  This prints all the print statements

'''

#
# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED


###################################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
signup() is not executed.
Because signup is not following the pytest rules.
pytest can only recognize the functions which are following the pytest rules
'''

###################################################################################################

# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")
#
# ## collected 1 item
# ## test_basics.py::test_login      login executing     PASSED

'''
Incase of nested test_functions, pytest can recognize only the outer test_function
pytest cannot recognize the inner test_function
'''

###################################################################################################

# def test_login():
#     pt("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
#
# ## collected 3 items
# ## test_basics.py::test_login                          FAILED
# ## test_basics.py::test_signup     signup executing    PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
Failure of one testcase will not stop the execution of the other testcases
'''

###################################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_signup     signup executing    PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
NOTE    :   When we call the test functions explicitly, the execution will happen twice 
'''

###################################################################################################

# def test_add(a, b):
#     print(a + b)
#
# test_add(1, 2)
#
# ## collecting ... 3
# ## collected 1 item
# ## test_basics.py::test_add        ERROR

'''
NOTE    :   test_functions donot take parameters
'''

###################################################################################################

# def test_sample():
#     print("hello world")
#
# def test_sample():
#     print("hello universe")
#
# ## collected 1 item
# ## test_basics.py::test_sample     hello universe      PASSED

'''
NOTE    :   If we are having multiple occurances of the same test_function name, pytest will always consider the latest one
'''

###################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing     PASSED
# ## test_basics.py::TestSample::test_signup     signup executing    PASSED
# ## test_basics.py::TestSample::test_logout     logout executing    PASSED

###################################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
Because the classname is not following the pytest rules
'''

###################################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
Because attributes are not following the rules
'''

###################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
#
# s_obj = TestSample()
# s_obj.test_login()
# s_obj.test_signup()
# s_obj.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing     PASSED
# ## test_basics.py::TestSample::test_signup     signup executing    PASSED
# ## test_basics.py::TestSample::test_logout     logout executing    PASSED

'''
When we create the object for the TestClass and call the attributes, execution will happen twice
'''

###################################################################################################

# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_login      ERROR

'''
test_attributes will not take any parameters
'''

###################################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items
# ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor


###################################################################################################


import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)


class TestRegister:

    def test_reg(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self):
        driver.find_element('id', 'gender-female').click()

    def test_fname(self):
        driver.find_element('id', 'FirstName').send_keys('Pooja')

    def test_lname(self):
        driver.find_element('id', 'LastName').send_keys('Mane')

    def test_reg_email(self):
        driver.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_reg_pwd(self):
        driver.find_element('id', 'Password').send_keys('pooja@12345')

    def test_confirm_pwd(self):
        driver.find_element('id', 'ConfirmPassword').send_keys('pooja@12345')
        time.sleep(2)


class TestLogin:

    def test_login(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self):
        driver.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_login_pwd(self):
        driver.find_element('id', 'Password').send_keys('pooja@12345')





















































