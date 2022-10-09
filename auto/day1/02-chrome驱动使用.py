from selenium import webdriver
import time

# 打开浏览器
# 打开浏览器，创建浏览器驱动对象
driver = webdriver.Chrome()
time.sleep(3)

# 关闭浏览器
driver.quit()