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

# xpath定位
# driver.find_element_by_xpath('xpath语法')
# 绝对路径：form标签
"""
print(driver.find_element_by_xpath('/html/body/form').get_attribute('outerHTML'))
"""
# 相对路径：from标签
"""
print(driver.find_element_by_xpath('//form').get_attribute('outerHTML'))
"""

# 相对路径绝对路径混合使用
# from标签
# print(driver.find_element_by_xpath('/html//form').get_attribute('outerHTML'))
# option标签
# 单数
print(driver.find_element_by_xpath('//body//option').get_attribute('outerHTML'))
print(driver.find_element_by_xpath('/html//form//select//option').get_attribute('outerHTML'))
# 复数
pprint(driver.find_elements_by_xpath('//body//option'))

# 关闭浏览器
driver.quit()
