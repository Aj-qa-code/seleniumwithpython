import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://stackoverflow.com/users/login')

