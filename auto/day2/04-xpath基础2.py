import time

from selenium import webdriver
import os
from pprint import pprint

# 打开浏览器
driver = webdriver.Chrome()

# 动态生成路径
# 获取html资源的绝对路径
html = os.path.abspath('html')
# 拼接路径
url = os.path.join(html, 'form.html')

# 请求目标网址
driver.get(url)

# .. 当前节点的父节点
"""
print(driver.find_element_by_xpath('//form/select/..').get_attribute('outerHTML'))
"""
# print(driver.find_element_by_xpath('//form/select/option/../option').get_attribute('outerHTML'))

# . 当前节点
# print(driver.find_element_by_xpath('//form/select/.').get_attribute('outerHTML'))

# 关闭浏览器
driver.quit()
