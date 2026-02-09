'''
iframe  :

'''
import time

## EG1

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.implicitly_wait(10)

driver.get('https://www.linkedin.com')
time.sleep(2)

## locate the iframe
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the frame
driver.switch_to.frame(google_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()

## scroll until youtube frame is visible
ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac.scroll_to_element(ele).perform()
time.sleep(2)

## locate iframe
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the iframe
driver.switch_to.frame(youtube_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//button[@title="Play"]').click()

## switch back to the parent frame
driver.switch_to.parent_frame()

###################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E21-Dec12-7PM\files_\iframe.html')
time.sleep(2)

## locate the iframe
frame1 = driver.find_element('xpath', '//iframe[@id="FR1"]')

## switch the driver to the iframe
driver.switch_to.frame(frame1)

## perform the operations inside the frame
driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('Books')
time.sleep(1)

## switch back to the parent frame
driver.switch_to.parent_frame()

## locate the frame
frame2 = driver.find_element('xpath', '//iframe[@id="FR2"]')

## switch the driver to the frame
driver.switch_to.frame(frame2)

## perform the operations inside the frame
driver.find_element('xpath', '//input[@id="search_form"]').send_keys('vehicle insurance')

## switch back to the parent frame
driver.switch_to.parent_frame()












