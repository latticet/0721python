from selenium import webdriver

# 准备无头模式的配置对象
# 创建options对象
options = webdriver.ChromeOptions()
# 添加无头模式的参数
options.add_argument('-headless')

# 打开浏览器
driver = webdriver.Chrome(options=options)

# 请求目标网址
driver.get('https://www.baidu.com')

# 输出当前页面的标题
print(driver.title)

# 退出浏览器
driver.quit()