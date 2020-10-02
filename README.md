## Initialize the browser with Selenium

#### These are the steps to follow to be able to initialize the browser with automated testing using python and selenium web driver.

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver ='/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://stackoverflow.com/users/login')

driver.find_element_by_xpath('').click()  
time.sleep(5)    #import time
driver.close()  #to close current browser
driver.quit()   #to close all browsers
print(driver.title)  #title of the page
print(driver.current_url)  #the URL of the page
driver.back()   #back to a previous page
driver.forward()  #to the following page
print(ele.is_displayed())  #to check is exist
print(ele.is_enabled())   #to check is available
print(ele.send_keys('username or pswrd'))
```

