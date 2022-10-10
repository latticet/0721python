from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 定位匹配到的第一个元素,如果没有匹配到会抛出错误
print(driver.find_element_by_id('kw'))
# print(driver.find_element_by_id('kw1')) # 匹配不到报错

# 定位匹配到的所有元素,返回一个列表.匹配不到,返回空列表
print(driver.find_elements_by_id('kw'))
print(driver.find_elements_by_id('kw1'))  # 匹配不到返回空列表

driver.quit()
