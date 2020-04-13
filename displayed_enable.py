from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http://newtours.demoaut.com/')

print(driver.title)
print(driver.current_url)

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #true or false return
print(user_ele.is_enabled()) #true or false return

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed()) #true or false return
print(pass_ele.is_enabled()) #true or false return

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")
time.sleep(3)
driver.find_element_by_name("login").click()

driver.quit()

















