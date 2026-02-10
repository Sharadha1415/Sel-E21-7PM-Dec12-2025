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

a = 10              ## global variable

def display():
    yield a
    yield 10
    yield 'hello'

# print(display())

for ele in display():
    print(ele)
print('hello world')
n =4
for i in range (n):
    print("* (n-i+1)+*(i-1))
for i in range (n-2, -1+1)):
    print("*" (n-i-1))
    print()
    















































