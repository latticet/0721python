import time
from selenium import webdriver

# TODO 准备模拟移动端需要的配置信息
# 创建配置对象
options = webdriver.ChromeOptions()
# 添加配置项
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone SE'})

# 打开浏览器
driver = webdriver.Chrome(options=options)

# 请求目标网址
driver.get('https://www.baidu.com')
time.sleep(5)

# 退出浏览器
driver.quit()