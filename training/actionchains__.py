'''
The operations which are performed using mouse/keyboard, we call them as low-level operations.
The operations such as hovering, right click, double click, scrolling operations, drag and drop operations,
enter key, ctrl, backspace, delete,...


To perform low-level operations in selenium, we use ActionChains

'''

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)


# ## Mouse hovering operations
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
# time.sleep(2)
#
# genz = driver.find_element('xpath', '(//a[text()="Genz"])[1]')
# ac_obj.move_to_element(genz).perform()

#################################################################################################

'''
double click
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(ele).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(ele2).perform()

#################################################################################################

'''
right click
'''
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# # ac_obj.context_click().perform()        ## will right click at the start of the application
#
# ##
# ele = driver.find_element('xpath', '//h2[text()="Tabs"]')
# ac_obj.context_click(ele).perform()


#################################################################################################

'''
Scrolling
'''

'''     scrolling to a specific web-element         '''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# ac_obj.scroll_to_element(ele).perform()

##--------------------------------------------------------------------------------

'''     Using execute_script'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# driver.execute_script("arguments[0].scrollIntoView();", ele)

#################################################################################################

'''
Scroll till the end of the application
'''
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## To go back to the start of the page
# ac_obj.send_keys(Keys.HOME).perform()

##---------------------------------------------------------------------------------

'''     Using execute script'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# ## To go back to the start of the page
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

#################################################################################################

'''
pagedown and pageup scrolling
'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()

##---------------------------------------------------------------------------

'''     Scrolling by pixels'''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 500);")       ## will scroll down by 500 pixels
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, -500);")       ## will scroll up by 500 pixels

##---------------------------------------------------------------------------

'''     scroll_by_amount()      '''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.scroll_by_amount(0, 1000).perform()

##---------------------------------------------------------------------------

'''     scroll from origin'''

# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h4[text()="RISING STARS"]')
#
# origin = ScrollOrigin.from_element(ele)
#
# ac_obj.scroll_from_origin(origin, 0, 2000).perform()

#################################################################################################

'''
drag and drop
'''

## drag_and_drop

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(1)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

##-------------------------------------------------------------------------

# ## drag_and_drop_by_offset
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(1)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
#
# ac_obj.drag_and_drop_by_offset(draggable_ele, 100, 50).perform()


#################################################################################################

'''     SLIDER      '''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# slider = driver.find_element('xpath', '//div[@id="slider-range"]/span[1]')
#
# ## Move the slider to the right
# ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
# time.sleep(2)
#
# ## Move the slider to the left
# ac_obj.click_and_hold(slider).move_by_offset(-100, 0).release().perform()


#################################################################################################

'''
ANALYZE THE BELOW CODE
'''

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
#
# ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
# time.sleep(1)
# ac_obj.send_keys('Potter').perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# #
# # ##-------------------------------------------------------------------
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
# fname.send_keys('Harry')
# time.sleep(2)
#
# fname.send_keys(Keys.CONTROL + 'a')         ## select the data
# fname.send_keys(Keys.CONTROL + 'c')         ## copy the data
#
# ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
# lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

# # ##-------------------------------------------------------------------
#
# ## ctrl + a
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
#
# # ############################################################################################################
#
# ## ctrl + backspace
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
#
# # ##-------------------------------------------------------------------
#
# ## shift
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
# time.sleep(2)
# ac_obj.key_down(Keys.SHIFT).send_keys('a').perform()
#
# # ##-------------------------------------------------------------------
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(2)
# ac_obj.send_keys('harry@gmail.com').perform()




































