import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.baidu.com')
# 执行js
# 语法： driver.execute_script(js代码)
driver.execute_script('alert("hello selenium")')

# 退出浏览器
time.sleep(3)
driver.quit()
