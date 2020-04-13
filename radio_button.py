from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http://newtours.demoaut.com/')

driver.implicitly_wait(10)

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #true or false return
print(user_ele.is_enabled()) #true or false return

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed()) #true or false return
print(pass_ele.is_enabled()) #true or false return

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]") #radio button check diff atributes
print("status of round trip radio button", roundtrip_radio.is_selected())


oneway_radio=driver.find_element_by_css_selector("input[value=oneway]") #radio button check diff atributes
print("status of one way radio button", oneway_radio.is_selected())

driver.quit()

#conditional commands with a return of true or false
#radio button - check boxes 
