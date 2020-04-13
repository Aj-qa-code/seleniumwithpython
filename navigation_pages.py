from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://the-internet.herokuapp.com')
print(driver.title)

driver.get('https://testsheepnz.github.io/BasicCalculator.html')
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.close()


