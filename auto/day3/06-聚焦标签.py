import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.163.com')
driver.maximize_window()
time.sleep(2)

# 滚动条聚焦到某个标签
# 定位要聚焦的标签
target = driver.find_element_by_link_text('外交部：已有1300多名印留学生获得来华签证')
print(target.get_attribute('outerHTML'))
driver.execute_script('arguments[0].scrollIntoView();', target)

time.sleep(10)
driver.quit()

