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
url = os.path.join(html, 'demo1.html')

# 请求目标网址
driver.get(url)

# TODO 选择当前元素之后的同级元素   //A/following-sibling::B
# <p>段落3</p> <p>段落4</p>
elements_p = driver.find_elements_by_xpath('//div[@id]/following-sibling::p')
for element_p in elements_p:
    print(element_p.get_attribute('outerHTML'))

print('==' * 20)

# TODO 选择当前元素之前的同级元素 //A/preceding-sibling::B
elements_p2 = driver.find_elements_by_xpath('//div[@id]/preceding-sibling::p')
for element_p in elements_p2:
    print(element_p.get_attribute('outerHTML'))

# 关闭浏览器
driver.quit()
