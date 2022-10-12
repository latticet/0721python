from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.baidu.com')
driver.find_element_by_link_text('新闻').click()

# 打印当前窗口的标题
print(driver.title)

# 切换到新闻窗口
# 获取当前浏览器的所有窗口
news_handles = driver.window_handles[1]
driver.switch_to.window(news_handles)

# 打印当前窗口的标题
print(driver.title)

# 退出浏览器
driver.quit()
