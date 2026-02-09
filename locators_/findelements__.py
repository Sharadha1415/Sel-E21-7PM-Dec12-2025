import time

'''
wap to enter the data for the textboxes present in demo.html
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\demo.html')
# time.sleep(2)
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')       ## list of web-elements
# ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9]
# print(all_textboxes)
#
# data_list = ['Tron', 'Vivah', 'Naruto', 'lion king', 'barbie', 'dhuranth', 'stranger things', 'money heist', 'crown']
#
# for textbox,data in zip(all_textboxes, data_list):
#     textbox.send_keys(data)

######################################################################################################

'''
wap to click on all checkboxes in demo.html
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\demo.html')
# time.sleep(2)
# all_checkboxes = driver.find_elements('xpath', '//input[@name="download"]')     ## list of web-elements
# ## [wb1, wb2, wb3, wb4, wb5, wb6]
#
# for checkbox in all_checkboxes:
#     checkbox.click()
#     time.sleep(1)

######################################################################################################
'''
wap to fetch the elements present in the footer of https://demowebshop.tricentis.com/
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')   ## list of web-elements
# ## [wb1, wb2, wb3, wb4,...wb22]
#
# for ele in footer_elements:
#     print(ele.text)

######################################################################################################
'''
wap to fetch the elements present in the categories section of https://demowebshop.tricentis.com/
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# all_categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
#
# for ele in all_categories:
#     print(ele.text)

######################################################################################################

'''
wap to print all the popular searches in myntra
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5,...]

for ele in popular_searches:
    print(ele.text)


'''
wap to print the shoe name and shoe price of adidas original shoes in myntra
wap to print the colors available for adidas original shoes in https://www.myntra.com/
wap to print the menu items of the items available in domino's pizza in https://www.zomato.com/bangalore/delivery 
wap to fetch all the recommended movies in https://in.bookmyshow.com/ 
'''






























