"""
使用注册实例.html练习所有API操作
"""
import os
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
url = os.path.join(os.path.abspath('html'), '注册实例.html')
driver.get(url)
time.sleep(1)

# TODO 主要操作
driver.find_element_by_id('user').send_keys('username')
time.sleep(1)
driver.find_element_by_id('fw').click()
time.sleep(1)
driver.find_element_by_id('alert').click()
# 切换
alert = driver.switch_to.alert
alert.accept()

# TODO A页操作
# 切换到A页面
driver.switch_to.frame('myframe1')
driver.find_element_by_id('userA').send_keys('usernameA')

# TODO B页操作
# 先要切换到主页，在切换到B页面
# driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.switch_to.frame('myframe2')

driver.find_element_by_id('passwordB').send_keys('1111')

# 退出浏览器
time.sleep(5)
driver.quit()
