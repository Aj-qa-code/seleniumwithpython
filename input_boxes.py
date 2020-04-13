from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

input_boxes=driver.find_elements_by_class_name("text_field")
print(len(input_boxes))
time.sleep(3)

driver.find_element_by_id("RESULT_TextField-1").send_keys("pavan")
time.sleep(4)
driver.find_element_by_id("RESULT_TextField-2").send_keys("kumar")
time.sleep(4)

driver.quit()

