import os.path
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 访问目标网址
url = os.path.join(os.path.abspath('html'), 'frame.html')
driver.get(url)
time.sleep(2)

# 定位操作
# <h3>frame</h3>
"""
print(driver.find_element_by_tag_name('h3').get_attribute('outerHTML'))
"""
# <h3 id="inner_h3">inner</h3> 定位不到，原因是这个标签在一个frame页面中
# print(driver.find_element_by_id('inner_h3'))


# TODO 切换frame
# 切换到inner这个frame页面
# iframe标签的id属性
"""
driver.switch_to.frame('f1')
"""
# iframe表的name属性
"""
driver.switch_to.frame('inner')
"""
# iframe定位得到的标签对象
inner_element = driver.find_element_by_id('f1')
driver.switch_to.frame(inner_element)
print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))

# 切换到inner_sub这个frame
driver.switch_to.frame('f2')
print(driver.find_element_by_id('p1').get_attribute('outerHTML'))

# TODO driver.switch_to.parent_frame() 切换到父级的frame
driver.switch_to.parent_frame()   # inner
print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))


# TODO driver.switch_to.default_content() 切换到主页面
driver.switch_to.frame('f2')  # inner_sub
driver.switch_to.default_content() # frame

print(driver.find_element_by_tag_name('h3').get_attribute('outerHTML'))
print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))  # 定位不到

# 退出浏览器
time.sleep(2)
driver.quit()
