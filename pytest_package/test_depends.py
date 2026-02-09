'''
Dependency  :   We can create the dependencies between the testcases.
                One testcase can be dependent on other testcases.

                To install dependency   -->     pip install pytest-dependency

                SYNTAX  :   @pytest.mark.dependency()               ## Independent testcase
                            def test_func1():
                                pass

                            @pytest.mark.dependency(depends=['test_func1'])         ## Dependent testcase
                            def test_func2():
                                pass

                            test_func2 is dependent on test_func1

                            If the independent testcase executes without any error, then dependent also executes without any error
                            If independent testcase itself is not working fine, then the dependent testcase will be skipped


'''


import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    yield driver
    driver.close()

@pytest.mark.dependency()                           ## independent testcase
def test_login(setup):
    setup.find_element("id", "user-name").send_keys('standard_user')
    time.sleep(1)
    setup.find_element("id", "password").send_keys('secret_sauceeee')
    time.sleep(1)
    setup.find_element("id", "login-button").click()
    time.sleep(3)
    wait = WebDriverWait(setup, 5)
    wait.until(expected_conditions.url_contains("inventory"))


@pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
def test_logout(setup):
    setup.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    setup.find_element('id', 'logout_sidebar_link').click()

#################################################################################################

# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login     login executing         PASSED
# ## test_depends.py::test_logout    logout executing        PASSED


#################################################################################################

# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     raise Exception
#
# @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login     FAILED
# ## test_depends.py::test_logout    SKIPPED (test_logout depends on test_login)


#################################################################################################

# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                           ## independent testcase
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## dependent testcase
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_login     login executing         PASSED
# ## test_depends.py::test_signup    signup executing        PASSED
# ## test_depends.py::test_logout    logout executing        PASSED

#################################################################################################
#
# @pytest.mark.dependency()                           ## independent testcase
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency()                           ## independent testcase
# def test_signup():
#     pnt("signup executing")
#
# @pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## dependent testcase
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_login     login executing     PASSED
# ## test_depends.py::test_signup                        FAILED
# ## test_depends.py::test_logout                        SKIPPED (test_logout depends on test_signup)

#################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing     PASSED
# ## test_depends.py::TestSample::test_logout                        SKIPPED (test_logout depends on test_login)

#################################################################################################
#
# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing         PASSED
# ## test_depends.py::TestSample::test_logout    logout executing        PASSED

#################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()                           ## independent testcase
#     def test_login(self):
#         prt("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])     ## dependent testcase
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     FAILED
# ## test_depends.py::TestSample::test_logout    SKIPPED (test_logout depends on TestSample::test_login)





































