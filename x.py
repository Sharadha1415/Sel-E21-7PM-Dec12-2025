# class Chrome:
#
#     @property
#     def current_url(self):
#         return "gmail executing"
#
# g = Chrome()
# print(g.current_url)
#
#
#
# with open('file', 'r') as f:

##########################################################################
'''
\n --> new line/next line
\t --> tab space

'''
import pytest

## raw strings

# print(r"Happy bir\thday \nandini. How are \U")

##########################################################################


# var1 = 'Nandini'
# var2 = 'Nadashr'
#
# for i, j in zip(var1, var2):
#     print(i, j)

'''
N N 
a a
n d
d a
i s
n h
i r
'''

##########################################################################


# def addition(a:int, b:int):
#     print(a + b)
#
# addition(10, 20)
# addition('a', 'b')
#
# def presence_of_element_located(locator: Tuple[str, str]):
#     pass
#
# presence_of_element_located(("id", "value"))


########################################################################
'''
launch amazon page search iphone15 pink with amount question is 1st title , then color and comeback to parent and select price.

'''


# print("My name is Nivedini")
# print("My name is Faizan")
# print("My name is Swarna")
# print("My name is Sanjay")
# print("My name is Pooja")
# print("My name is Nandini")
# print("My name is Vijayalakshmi")
# print("My name is Sanchitha")
# print("My name is Ligy")

# name = input("enter the name : ")
# age = int(input("Enter your age : "))
# print(f"My name is {name}. I am {age*4} years old")


############################################################

# class Calculator:
#
#     ## attributes
#     def addition(self, a, b):
#         print(a + b)
#
#     def subtraction(self, a, b):
#         print(a - b)
#
# c = Calculator()
# c.addition(1, 2)
# c.subtraction(10, 20)
# c.multiplication()      ## AttributeError

############################################################

# ## name = "value"
# stu_1 = 'Nivedini'
# print(stu_1)
# print(stu_2)


#
# subject = "python"      ## global variable
#
# def sample():
#     a = 100             ## local variable
#
# class Sample:
#
#     name = 'Sanjay'             ## class variable
#
#     def __init__(self, place, email):       ## object variables
#         self.place = place
#         self.email = email
#
#     def display(self, college_name):        ## method variables
#         print(f'My name is {self.name}')
#
#
# s = Sample('Bengaluru', 'Sanjay@gmail.com')
# s.display('MIT')

#######################################################################

import time

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
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys('Pooja')
# driver.find_element('id', 'LastName').send_keys('Mane')
# driver.find_element('id', 'Email').send_keys('pooja@gmail.com')
# driver.find_element('id', 'Password').send_keys('pooja@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('pooja@12345')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# time.sleep(1)
# driver.find_element('id', 'Email').send_keys('pooja@gmail.com')
# driver.find_element('id', 'Password').send_keys('pooja@12345')

#######################################################################

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


####################################################################

# def display():
#     num1 = 1000
#     global num1
#
# print(num1)

####################################################################

# a = 10              ## global variable
#
# def display():
#     yield a
#     yield 10
#     yield 'hello'
#
# # print(display())
#
# for ele in display():
#     print(ele)
# print('hello world')
# n =4
# for i in range (n):
#     print("* (n-i+1)+*(i-1))
# for i in range (n-2, -1+1)):
#     print("*" (n-i-1))
#     print()
#     


####################################################################

from selenium import webdriver
driver = webdriver.Chrome()

'''switch the driver to the alert'''
# alert_obj = driver.switch_to.alert
# alert_obj.send_keys("nandini")
# alert_obj.accept()
# alert_obj.dismiss()
#
# 'https://username:password@url'

##------------------------------------------------------------------

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# ac = ActionChains(driver)
# k = Keys()

# ele = driver.find_element('', '')
# ac.move_to_element(ele).perform()
# ac.double_click(ele).perform()
# ac.context_click(ele).perform()
# ac.drag_and_drop('drag', 'drop').perform()
# ac.drag_and_drop_by_offset(ele, 100, 100).perform()
# ac.scroll_to_element(ele).perform()
# ac.scroll_by_amount(0, 0).perform()
# ac.send_keys(Keys.PAGE_DOWN).perform()
# ac.send_keys(Keys.PAGE_UP).perform()
# ac.send_keys(Keys.END).perform()
# ac.send_keys(Keys.HOME).perform()
#
# ac.click_and_hold('slider').move_by_offset(100, 0).release().perform()
#
# ac.send_keys(Keys.ENTER).perform()
# ac.send_keys(Keys.BACKSPACE).perform()
# ac.send_keys(Keys.TAB).perform()
# ac.send_keys(Keys.SPACE).perform()
# ac.send_keys(Keys.DELETE).perform()
# ac.send_keys(Keys.ENTER).perform()
# ac.send_keys(Keys.CONTROL).perform()

##------------------------------------------------------------------

''' standard listboxes  - tagname is select     '''

# from selenium.webdriver.support.select import Select
#
# listbox = driver.find_element('tag name', 'select')
# select_obj = Select(listbox)
#
# select_obj.select_by_index(10)
# select_obj.select_by_value("value")
# select_obj.select_by_visible_text("text")
#
# select_obj.deselect_by_index(10)
# select_obj.deselect_by_value("value")
# select_obj.deselect_by_visible_text("text")
#
# select_obj.deselect_all()
#
# first = select_obj.first_selected_option
# all = select_obj.all_selected_options
# options = select_obj.options
# select_obj.is_multiple()

##------------------------------------------------------------------

''' iframe  --> tagname of an iframe is always iframe   '''

# frame = driver.find_element('tag name', 'iframe')
#
# ## switch the driver to the frame
# driver.switch_to.frame(frame)
#
# ## perform the operations inside the frame
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()

##------------------------------------------------------------------
'''     window handling     '''

# ## switch the driver from the parent app to the child application
#
# handles = driver.window_handles     ## [handle1, handle2, handle3, handle4,..]
#
# driver.switch_to.window('')

##------------------------------------------------------------------
'''     synchronization    
        *   unconditional   --> time.sleep(30) 
        *   conditional     --> 
            *   implicit    --> driver.implicitly_wait(30)
            *   explicit    -->
'''

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[])
# # wait.until(expected_conditions.condition)

##------------------------------------------------------------------
'''
xlrd    :   import xlrd
            workbook = xlrd.open_workbbok("path")               ## book object
            worksheet = workbook.sheet_by_name("SheetName")     ## sheet object
            convert the sheet object to the generator object
            rows = worksheet.get_rows()                         ## generator object
            Traverse/typecast/next()
'''

##------------------------------------------------------------------

'''
openpyxl    :   from openpyxl import Workbook
                workbook = Workbook()           ## create an excel file
                worksheet = workbook.active     ## initialize the active worksheet
                title = worksheet.title         ## set the title(optional)
                worksheet[A1] = 'data1'
                worksheet[A2] = 'data2'
                
                data_list = [[], [], []]
                
                for data in data_list:
                    worksheet.append(data)
                
                workbook.save("filename.xlsx")
                workbook.save(r"location\excel_name.xlsx")
'''

##------------------------------------------------------------------
'''
pytest  :   unit testing framework
            *   filename --> test_filename.py   or filename_test.py
            *   function --> test_func()
            *   class    --> class TestClassname:
                                pass

'''

# @pytest.fixture(autouse=True, scope='class')
# def setup():
#     pass
#     yield
#     pass


# @pytest.mark.sanity
# def test_func1():
#     pass
#
# ## pytest test_filename.py -vs -m="markername"


# @pytest.mark.skipif('condition', reason='')
# def test_func1():
#     pass

# @pytest.mark.xfail
# def test_func1():
#     pass

# @pytest.mark.parametrize("formal", [("")])
# def test_func1(formal):
#     pass










































