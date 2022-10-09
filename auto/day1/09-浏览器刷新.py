import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 访问目标地址
driver.get('https://www.baidu.com')
time.sleep(2)

# TODO 浏览器刷新
driver.refresh()
time.sleep(2)

# 退出浏览器
driver.quit()