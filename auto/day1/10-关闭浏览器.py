import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.baidu.com')
time.sleep(2)

# 点击新闻超链接
# 定位新闻标签，然后点击
driver.find_element_by_link_text('新闻').click()
time.sleep(2)

# TODO 关闭当前窗口
driver.close()
time.sleep(3)

# 退出浏览器
driver.quit()