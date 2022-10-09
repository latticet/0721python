import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 访问目标地址
driver.get('https://www.baidu.com')
time.sleep(2)

# TODO 后退
driver.back()
time.sleep(2)

# TODO 前进
driver.forward()
time.sleep(2)

# 退出浏览器
driver.quit()