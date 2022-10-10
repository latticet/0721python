import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.baidu.com')
time.sleep(1)

# 单数元素定位，定位成功返回WebElement对象，定位失败抛出异常：NoSuchElementException
# TODO id元素定位
"""
print(driver.find_element_by_id('kw').get_attribute('outerHTML'))
"""
# TODO 通过class定位
# WebElement.get_attribute('属性名')  获取标签对象的属性值
# outerHTML:获取元素对象的html标签
"""
s_tab = driver.find_element_by_class_name('s_tab ')
print(s_tab.get_attribute('outerHTML'))
"""

# TODO 通过链接文本定位
"""
print(driver.find_element_by_link_text('新闻').get_attribute('outerHTML'))
"""

# TODO 通过部分链接文本定位
"""
print(driver.find_element_by_partial_link_text('hao').get_attribute('outerHTML'))
"""

# TODO 通过标签的name属性定位
# 一般只有表单标签才会有name属性，表单提交到后端后，通过name名称来获取数据
"""
print(driver.find_element_by_name('rn').get_attribute('outerHTML'))
"""

# TODO 通过标签名定位
"""
print(driver.find_element_by_tag_name('a').get_attribute('outerHTML'))
"""

# 关闭浏览器
driver.quit()
