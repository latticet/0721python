from selenium import webdriver
import os
import time

# 打开浏览器，访问网址
driver = webdriver.Chrome()
url = os.path.join(os.path.abspath('html'), 'form.html')
driver.get(url)

# TODO 定位上传文件标签，然后send_keys传入有上传的资源（绝对路径）
time.sleep(1)
cat_url = os.path.join(os.path.abspath('html'), 'cat.png')
driver.find_element_by_xpath('//input[@type="file"]').send_keys(cat_url)

# 退出浏览器
time.sleep(3)
driver.quit()
