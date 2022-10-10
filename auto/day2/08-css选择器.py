from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.baidu.com')

# css选择器定位
# 基础
"""
print(driver.find_element_by_css_selector('#kw').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('i').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('.s-p-top').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('*').get_attribute('outerHTML'))
"""

# 复合选择器
# E1 E2
"""
print(driver.find_element_by_css_selector('#form input').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('#form #kw').get_attribute('outerHTML'))
"""

# css3新选择器
# 属性
# print(driver.find_element_by_css_selector('input[name="wd"]').get_attribute('outerHTML'))
# 定位某个标签下的第8个input标签
print(driver.find_element_by_css_selector('input:nth-child(8)').get_attribute('outerHTML'))

# 关闭浏览器
driver.quit()
