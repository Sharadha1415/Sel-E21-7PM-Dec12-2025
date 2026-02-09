import time


'''     Initializing Chrome browser'''

from selenium import webdriver
c_driver = webdriver.Chrome()

## Chrome browser will close automatically

#-------------------------------------------------------------------------------

# ## To prevent the browser from automatically closing
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# c_driver = webdriver.Chrome(opts)

#################################################################################

'''     Initializing Firefox browser'''

# from selenium import webdriver
# f_driver = webdriver.Firefox()
#
# ## Firefox browser will not close automatically.
# ## So, no need to write FirefoxOptions and add_experimental_option attribute

#################################################################################

'''     Initializing Edge browser'''

# from selenium import webdriver
# e_driver = webdriver.Edge()

## Edge browser will close automatically

#-------------------------------------------------------------------------------

# ## To prevent the browser from automatically closing
#
# from selenium import webdriver
#
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
#
# e_driver = webdriver.Edge(opts)




















