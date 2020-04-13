import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://gmail.com')

user = browser.find_element_by_id('identifierId')
user.send_keys('andreasilvinaj@gmail.com')
user.send_keys(Keys.ENTER)
time.sleep(4)

password = browser.find_element_by_name('password')
password.send_keys('karamelo1988')
password.send_keys('Key.ENTER')
time.sleep(3)

