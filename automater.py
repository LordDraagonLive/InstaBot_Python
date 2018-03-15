from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#new browser session
browser = webdriver.Chrome('./assets/chromedriver')

#navigating to a webpage
browser.get('https://www.Instagram.com')

#make sure the browser stays open for 5 secs
sleep(5)

#find log in link
login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')


#make sure the browser stays open for 5 secs to see the effect
# sleep(5)

#click it
login_elem.click()


#find form inputs and enter data
inputs = browser.find_elements_by_xpath('//form/div/input')

ActionChains(browser)\
    .move_to_element(inputs[0]).click()\
    .send_keys('contacting.john.doe')\
    .move_to_element(inputs[1]).click()\
    .send_keys('passtheword')\
    .perform()

#find the login button and click it
login_button = browser.find_element_by_xpath(
    '//form/span/button[text()="Log in"]')

ActionChains(browser)\
    .move_to_element(login_button)\
    .click().perform()

#clean exit
# browser.close()
