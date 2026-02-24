'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()



'''
import time

## Confirmation alert

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element("xpath", '//button[text()="Confirmation Alert"]').click()       ## gives alert
time.sleep(2)

## switch the driver to the alert
alert_obj = driver.switch_to.alert

alert_obj.accept()      ## clicks on OK/YES/AGREE,..
time.sleep(1)
alert_msg = driver.find_element('xpath', '//p[@id="demo"]')     ## Locating the message
print(alert_msg.text)
time.sleep(2)

driver.find_element("xpath", '//button[text()="Confirmation Alert"]').click()       ## gives alert
time.sleep(2)
alert_obj.dismiss()     ## clicks on CANCEL/NO/DISAGREE,..
alert_msg2 = driver.find_element('xpath', '//p[@id="demo"]')
print(alert_msg2.text)
time.sleep(2)

######################################################################################################

# ## Simple
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
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()     ## gives alert
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()     ## gives alert
# time.sleep(2)
# alert_obj.dismiss()

######################################################################################################

# ## prompt
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
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()     ## gives alert
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# alert_obj.send_keys("Nadashree")
# alert_obj.accept()

######################################################################################################

# ## Authentication pop-up
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## The above url will give a pop-up to enter the username and password.
# ## To enter the app, we need to give username and pwd.
# ## The pop-up is not inspectable. And we cant switch the driver to the alert

##------------------------------------------------------------------------------------

# ## To handle the authentication popups, we use the below syntax
# ## SYNTAX   :   https://username:password@url
# ## For the below url, username and password is both admin
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')


######################################################################################################

# ## push notifications
#
# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="OK"]').click()
#
#
# ##-----------------------------------------------------------------------
#
# ## Firefox
# from selenium import webdriver
#
# opts = webdriver.FirefoxOptions()
# opts.set_preference("dom.webnotifications.enabled", False)
# opts.set_preference("dom.push.enabled", False)
#
# driver = webdriver.Firefox(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="OK"]').click()
#
# ##-----------------------------------------------------------------------
#
# ## Edge
# from selenium import webdriver
#
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Edge(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="OK"]').click()

######################################################################################################

# ## Confirmation alert
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
# driver.find_element("xpath", '//button[text()="Confirmation Alert"]').click()       ## gives alert
# time.sleep(2)
#
#
# def handle_alert(userinput):
#     alert_obj = driver.switch_to.alert
#     if userinput == 'accept':
#         alert_obj.accept()
#     elif userinput == 'dismiss':
#         alert_obj.dismiss()
#
#
# handle_alert("accept")
# time.sleep(2)
# driver.find_element("xpath", '//button[text()="Confirmation Alert"]').click()       ## gives alert
# time.sleep(2)
# handle_alert("dismiss")
# time.sleep(2)





































