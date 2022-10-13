import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/selectTest.htm')

# 定位要操作的select标签
s1 = driver.find_element_by_id('s1')
# 通过select标签定位option
time.sleep(1)
s1.find_element_by_xpath('//option[@value=48]').click()

time.sleep(5)
driver.quit()
