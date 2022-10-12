from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 1。 打开浏览器
driver = webdriver.Chrome()

# 2. 请求百度
driver.get('https://www.baidu.com')
time.sleep(1)

# 3. 在搜索框输入 《天气预报》
kw = driver.find_element_by_id('kw')
kw.send_keys('天气预报')
time.sleep(1)

# 4. 选中搜索框的所有内容
kw.send_keys(Keys.CONTROL, 'a')
time.sleep(1)

# 5. 复制搜索框的所有内容
kw.send_keys(Keys.CONTROL, 'c')

# 6. 请求360搜索
driver.get('https://www.so.com')
time.sleep(1)

# 7. 把复制的内容粘贴到搜索框
driver.find_element_by_id('input').send_keys(Keys.CONTROL, 'v')

# 8. 点击搜索
driver.find_element_by_id('search-button').click()

# 9. 退出浏览器
time.sleep(2)
driver.quit()
