import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

for r in range(2, 8):
    for c in range(1, 5):
        data = driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
        print(data.text, end='\t\t')
    print()


'''
r=2, c=1    --> //table[@name="BookTable"]//tr[2]/td[1]
r=2, c=2    --> //table[@name="BookTable"]//tr[2]/td[2]
r=2, c=3    --> //table[@name="BookTable"]//tr[2]/td[3]
r=2, c=4    --> //table[@name="BookTable"]//tr[2]/td[4]

r=3, c=1    --> //table[@name="BookTable"]//tr[3]/td[1]
r=3, c=2    --> //table[@name="BookTable"]//tr[3]/td[2]
r=3, c=3    --> //table[@name="BookTable"]//tr[3]/td[3]
r=3, c=4    --> //table[@name="BookTable"]//tr[3]/td[4]

r=4, c=1    --> //table[@name="BookTable"]//tr[4]/td[1]
r=4, c=2    --> //table[@name="BookTable"]//tr[4]/td[2]
r=4, c=3    --> //table[@name="BookTable"]//tr[4]/td[3]
r=4, c=4    --> //table[@name="BookTable"]//tr[4]/td[4]


'''





























