
'''     DECORATORS      '''
# def outer(func):                    ## after execution of @outer, func --> addition
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)       ## addition(1, 2)
#     return wrapper          ## return takes the wrapper address, gives the value to the func call and gets out of the function
#
#
# @outer          ## addition = outer(addition)           ##  after return --> addition --> wrapper address
# def addition(a, b):
#     print(a + b)
#
# addition(1, 2)                  ## wrapper(1, 2)
# addition(10, -10)                  ## wrapper(10, -10)

####################################################################################################3

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def test_login():
#     print("login executing")
#
# @outer
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED


####################################################################################################

'''
Fixture :   @pytest.fixture()  is a inbuilt decorator
            It is a function which is used to perform setup and teardown operations
            setup       :   The set of operations which executes before the execution of the test_function
            teardown    :   The set of operations which executes after the execution of the test_function

            SYNTAX      :   @pytest.fixture()
                            def func():
                                pass            ## setup
                                yield
                                pass            ## teardown

                            def test_func(func):
                                pass

                            We should pass the name of the fixture as a parameter for the test_functions. Pytest willl automatically execute it.

                            *   autouse :   autouse is a argument of fixture. It is an optional argument.
                                            When we give autouse=True, by default the fixture will be applied for all the test_functions/test_methods present in that module

                            *   scope   :   It is an argument of a fixture. It is also an optional parameter.
                                            scope defines the scope of a fixture.

                                            When we give scope="class", the fixture will be applied on a class level.
                                            Before the execution of the entire class, setup operation will be performed
                                            After the execution of the entire class, teardown operation will be performed

                                            When we give scope="module", the fixture will be applied on a module(file) level.
                                            Before the execution of the entire module, setup operation will be performed
                                            After the execution of the entire module, teardown operation will be performed

                                            Be default, scope="function"

'''


import pytest

#
# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout       Good morning        logout executing    PASSED


###################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_signup                       signup executing    PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

'''
Fixture is not applied for test_signup.
'''
###################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

'''
NOTE    :   The operations before yield will be executed before the execution of the test function
            The operations after yield will be executed after the execution of the test function
'''

###################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

'''
When we give autouse=True, the fixture will be applied for each and every test_funct present in that module
'''

###################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# @pytest.fixture(autouse=True)
# def display():
#     print("Hi all")
#     yield
#     print("Bye all")
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Hi all      Good morning        login executing     PASSEDGood evening      Bye all
# ## test_fixtures.py::test_signup   Hi all      Good morning        signup executing    PASSEDGood evening      Bye all
# ## test_fixtures.py::test_logout   Hi all      Good morning        logout executing    PASSEDGood evening      Bye all


###################################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self ,greet):
#         print("signup executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login        Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_signup       Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout       Good morning        logout executing    PASSEDGood evening

###################################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
#
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
# ## test_fixtures.py::TestSample::test_login        Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_signup       Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout       Good morning        logout executing    PASSEDGood evening


###################################################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening

###################################################################################################

'''
scope is the parameter of the fixture.
When we give scope='class', the fixture will be applied on a class level.
*   It will perform the setup operation.
*   It will execute all the attributes of the TestClass
*   It will perform the teardown operation
'''

###################################################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_outlook(self):
#         print("outlook executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening
# ## test_fixtures.py::TestDisplay::test_gmail   Good morning        gmail executing     PASSED
# ## test_fixtures.py::TestDisplay::test_outlook                     outlook executing   PASSED
# ## test_fixtures.py::TestDisplay::test_yahoo                       yahoo executing     PASSEDGood evening

###################################################################################################

'''
apply fixture only for 1 class out of 2 classes.
Remove autose=True, give the name of the fixture as a parameter for the test_methods
'''

# @pytest.fixture(scope='class')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# class TestDisplay:
#
#     def test_gmail(self, greet):
#         print("gmail executing")
#
#     def test_outlook(self, greet):
#         print("outlook executing")
#
#     def test_yahoo(self, greet):
#         print("yahoo executing")
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login                    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSED
# ## test_fixtures.py::TestDisplay::test_gmail   Good morning    gmail executing     PASSED
# ## test_fixtures.py::TestDisplay::test_outlook                 outlook executing   PASSED
# ## test_fixtures.py::TestDisplay::test_yahoo                   yahoo executing     PASSEDGood evening

###################################################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_outlook(self):
#         print("outlook executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSED
# ## test_fixtures.py::TestDisplay::test_gmail                   gmail executing     PASSED
# ## test_fixtures.py::TestDisplay::test_outlook                 outlook executing   PASSED
# ## test_fixtures.py::TestDisplay::test_yahoo                   yahoo executing     PASSEDGood evening

###################################################################################################
#
# @pytest.fixture(autouse=True, scope='session')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_outlook(self):
#         print("outlook executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")

################################################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
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
# class TestDisplay:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_outlook(self):
#         print("outlook executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")

################################################################################################

import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome(opts)

class TestRegister:

    def test_reg(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-female').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Pooja')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('Mane')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('pooja@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('pooja@12345')
        time.sleep(2)


class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('pooja@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('pooja@12345')


































