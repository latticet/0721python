from selenium import webdriver
import os
import time

# 打开浏览器，访问网址
driver = webdriver.Chrome()
url = os.path.join(os.path.abspath('html'), 'form.html')
driver.get(url)

# TODO 单选按钮操作
time.sleep(1)
radio_boy = driver.find_elements_by_xpath('//input[@type="radio"]')[0]
radio_girl = driver.find_elements_by_xpath('//input[@type="radio"]')[1]
radio_boy.click()
print(radio_boy.is_selected())
print(radio_girl.is_selected())

# TODO 多选按钮操作
time.sleep(1)
checkbox1 = driver.find_elements_by_xpath('//input[@type="checkbox"]')[0]
checkbox2 = driver.find_elements_by_xpath('//input[@type="checkbox"]')[1]
checkbox1.click()
print(checkbox1.is_selected())
print(checkbox2.is_selected())

# 退出浏览器
time.sleep(3)
driver.quit()
