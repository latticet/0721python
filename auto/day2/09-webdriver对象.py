import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 点击新闻链接
driver.find_element_by_link_text('新闻').click()

# TODO WebDriver对象的属性
"""
print(driver.name)
print(driver.current_url)
print(driver.page_source)
"""
# 当前窗口句柄
print(driver.current_window_handle)
# 当前浏览器的所有窗口句柄
print(driver.window_handles)

# 切换窗口
# 老版本
# driver.switch_to_window(driver.window_handles[1])
# 新版本
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

driver.quit()