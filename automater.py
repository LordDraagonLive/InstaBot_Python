from time import sleep
from selenium import webdriver

#new browser session
browser = webdriver.Chrome('./assets/chromedriver')

#navigating to a webpage
browser.get('https://www.Instagram.com')


#make sure the browser stays open for 5 secs
sleep(5)

#clean exit
browser.close()
