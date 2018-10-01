from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#new browser session
browser = webdriver.Chrome('./assets/chromedriver')

#navigating to a webpage
browser.get('https://www.Instagram.com')

#make sure the browser stays open for 2 secs
sleep(2)

#find log in link
login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')


#make sure the browser stays open for 5 secs to see the effect
# sleep(5)

#click it
login_elem.click()

#make sure the browser stays open for 2 secs
sleep(2)

#find form inputs and enter data
inputs = browser.find_elements_by_xpath('//form/div/div/div/input')

ActionChains(browser)\
    .move_to_element(inputs[0]).click()\
    .send_keys('buddhiadhikari@live.com')\
    .move_to_element(inputs[1]).click()\
    .send_keys('#123#')\
    .perform()

#make sure the browser stays open for 2 secs
sleep(2)

#find the login button and click it
login_button = browser.find_element_by_xpath(
    '//form/span/button[text()="Log in"]')

ActionChains(browser)\
    .move_to_element(login_button)\
    .click().perform()

#make sure the web element 'body' is loaded before getting it
sleep(1)

#find the body element to send keys to (error : stale element reference: element is not attached to the page document
# occured because the tag wasn't loaded before we get it from the page )
body_elem = browser.find_element_by_tag_name('body')

#move up and down to load new images
for _ in range(3):
    # sleep(2)
    body_elem.send_keys(Keys.END)
    sleep(2)
    body_elem.send_keys(Keys.HOME)
    sleep(2)

#Find all like hearts

hearts = browser.find_elements_by_xpath('//a[contains(@class, "_eszkz _l9yih")]')

#Click all the hearts
for i,heart in enumerate(hearts):
    print('{}/{}'.format(i,len(hearts)))
    heart.click()
    sleep(2)

#clean exit
# browser.close()
