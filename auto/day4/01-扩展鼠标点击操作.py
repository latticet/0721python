import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://sahitest.com/demo/clicks.htm')

# 点击操作
ac = ActionChains(driver)
btn = driver.find_element_by_xpath('/html/body/form/input[3]')
ac.click(btn).click(btn).click(btn).perform()

time.sleep(5)
driver.quit()


