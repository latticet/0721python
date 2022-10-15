import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/selectTest.htm')

# 第一种： 普通方式
"""
s1 = driver.find_element_by_id('s1')
s1.find_element_by_xpath('//option[@value="48"]').click()
"""

# 第二种： select类
s1 = driver.find_element_by_id('s1')
select = Select(s1)
select.select_by_value('48')
select.select_by_index(3)
select.select_by_visible_text('Email')

time.sleep(2)
driver.quit()

