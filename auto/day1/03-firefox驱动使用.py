import time
from selenium import webdriver

# 打开浏览器
driver = webdriver.Firefox()
time.sleep(3)

# 退出浏览器
driver.quit()