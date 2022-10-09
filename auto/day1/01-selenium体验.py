from selenium import webdriver
import time


# 1. 打开chrome
driver = webdriver.Chrome()
time.sleep(2)

# 2. 在地址栏输入百度的网址，请求百度
# 注意：需要写完整网址
driver.get('https://www.baidu.com/')
time.sleep(2)

# 3. 在搜索框输入关键字《天气预报》
driver.find_element_by_id('kw').send_keys('天气预报')
time.sleep(2)

# 4. 点击百度一下
driver.find_element_by_id('su').click()
time.sleep(3)

# 5. 关闭浏览器
driver.quit()