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

# TODO 逻辑运算符
# 姓名2：<input type="text" value="hello"><br/>
"""
print(driver.find_element_by_xpath('//form/input[@type="text" and @value="hello"]').get_attribute('outerHTML'))
print(driver.find_element_by_xpath('//form/input[@type="text" and @value]').get_attribute('outerHTML'))
"""

# TODO 模糊匹配 contains()
# 介绍2：<textarea  cols="40" rows="10">hello unittest</textarea>
# text()
print(driver.find_element_by_xpath('//form/textarea[contains(text(), "unit")]').get_attribute('outerHTML'))
# @属性名
print(driver.find_element_by_xpath('//form/textarea[contains(@cols, "4")]').get_attribute('outerHTML'))
# TODO 以某个值开始 starts-with()
print(driver.find_element_by_xpath('//form/textarea[starts-with(@cols, "3")]').get_attribute('outerHTML'))
print(driver.find_element_by_xpath('//form/textarea[starts-with(text(), "hello")]').get_attribute('outerHTML'))

# TODO * 匹配所有的标签
print(driver.find_elements_by_xpath('/*'))
print(driver.find_element_by_xpath('/*').get_attribute('outerHTML'))

print(len(driver.find_elements_by_xpath('//*')))




# 关闭浏览器
driver.quit()
