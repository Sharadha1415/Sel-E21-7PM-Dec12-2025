import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

# ## To maximize the window
# driver.maximize_window()
# time.sleep(2)
#
# # ## To minimize the window
# # driver.minimize_window()
# # time.sleep(2)
#
# ## To go back
# driver.back()
# time.sleep(2)
#
# ## To go forward
# driver.forward()
# time.sleep(2)
#
# ## To refresh
# driver.refresh()
# time.sleep(2)

# ## current_url  :   It is a property. It gives the url of the page
# print(driver.current_url)
#
# ## title        :   It is a property. It gives the title of the page
# print(driver.title)
#
# ## name         :   It is a property. It gives the name of the browser
# print(driver.name)
#
# ## page_source  :   It is a property. It gives the page source
# print(driver.page_source)

##-----------------------------------------------------------------------------------------------

# ## To take screenshot of the page
# driver.save_screenshot('myntra_homepage.png')
# ## The screenshot will be saved in the same package as our python file

# ## To save the screenshot in different location
# driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\screenshots\myn_homepage.png')

##-----------------------------------------------------------------------------------------------

# ## To close the browser
# driver.close()






