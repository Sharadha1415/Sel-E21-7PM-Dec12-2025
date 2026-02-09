import time

'''
location    :   This is a property
                Gives the x and y co-ordinates of the element on the page
                SYNTAX  :   web_element.location
                
size        :   This is a property
                This gives the height and width of the web-element
                SYNTAX  :   web_element.size

rect        :   This is a property
                Combination of location and size
                SYNTAX  :   web_element.rect
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/register")
time.sleep(2)

male_radiobtn = driver.find_element('id', 'gender-male')

print(male_radiobtn.location)       ## {'x': 415, 'y': 317}

print(male_radiobtn.size)           ## {'height': 13, 'width': 13}

print(male_radiobtn.rect)           ## {'height': 13, 'width': 13, 'x': 414.5375061035156, 'y': 316.6875}





