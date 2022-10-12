import os
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
url = os.path.join(os.path.abspath('html'), 'popup.html')
driver.get(url)

buttons = driver.find_elements_by_tag_name('button')
btn1 = buttons[0]
# TODO 重点掌握alert弹窗
# 点击alert
btn1.click()

# 切换到当前弹窗
# 回顾
# 1. 切换窗口 driver.switch_to.window()
# 2. 切换frame driver.switch_to.frame()
# 3. 切换弹窗 driver.switch_to.alert()
alert = driver.switch_to.alert  # 切换到当前弹窗，返回当前弹窗
time.sleep(1)
alert.accept()  # 确定
time.sleep(1)

# 点击confirm
buttons[1].click()
confirm = driver.switch_to.alert
time.sleep(1)
# 确定
# confirm.accept()
# 取消
confirm.dismiss()
time.sleep(1)

# 点击prompt
buttons[2].click()
prompt = driver.switch_to.alert
time.sleep(1)

# 向prompt弹窗输入内容
prompt.send_keys('hello')
# 确定
prompt.accept()
# 取消
# prompt.dismiss()

time.sleep(5)
driver.quit()
