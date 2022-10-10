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

# TODO 谓词语法
# //AA/BB[谓词]
"""
print(driver.find_element_by_xpath('//select/option[2]').get_attribute('outerHTML'))  # 第二个option
print(driver.find_element_by_xpath('//select/option[last()]').get_attribute('outerHTML')) # 最后一个option
print(driver.find_element_by_xpath('//select/option[last()-1]').get_attribute('outerHTML')) # 倒数第二个
pprint(driver.find_elements_by_xpath('//select/option[position()<3]'))  # 定位前2个option
"""
# 谓词：标签属性定位
# 语法：/AA//BB[@属性名]   /AA//BB[@属性名=属性值]
print(driver.find_element_by_xpath('//option[@selected]').get_attribute('outerHTML'))

# 定位带有type属性的input的标签
print(driver.find_element_by_xpath('//input[@type]').get_attribute('outerHTML'))
print(driver.find_element_by_xpath('//input[@type="password"]').get_attribute('outerHTML'))

# 关闭浏览器
driver.quit()
