import time

from selenium import webdriver

# 准备配置项
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data')

# 打开浏览器
driver = webdriver.Chrome(options=options)

# 打开目标网址
driver.get('https://mail.163.com')

# 退出浏览器
time.sleep(3)
driver.quit()
