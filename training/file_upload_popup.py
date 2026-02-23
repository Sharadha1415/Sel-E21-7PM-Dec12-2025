import time

'''     upload single files     '''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# path = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html'
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(path)
#
#
# ###############################################################################################
#
'''    uploading multiple files    '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# f1 = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\css_selector.html'
# f2 = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\demo.html'
# f3 = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\loading.html'
# f4 = r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\progressbar.html'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{f1}\n{f2}\n{f3}\n{f4}')

###############################################################################################

'''     File download pop-up    '''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()
## The download will happen in the default downloads folder

# ##-------------------------------------------------------------------------------
#
# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory" : r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
#
# opts.add_experimental_option("prefs", prefs)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demoqa.com/upload-download')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()

##-------------------------------------------------------------------------------

## Firefox
from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("browser.download.folderList", 2)
opts.set_preference("browser.download.dir", r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\notes')

driver = webdriver.Firefox(opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()

































