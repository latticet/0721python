import os.path
import time

from selenium import webdriver

# TODO 准备配置项
options = webdriver.ChromeOptions()

# 动态生成下载的路径
download_path = os.path.join(os.path.abspath('download'))
prefs = {
    'profile.default_content_settings.popups': 0,  # 取消弹窗
    'download.default_directory': download_path
}
options.add_experimental_option('prefs', prefs)

# 打开浏览器, 请求目标网址
driver = webdriver.Chrome(options=options)
driver.get('https://www.selenium.dev/downloads/')
driver.implicitly_wait(100)

# 下载的操作
driver.find_element_by_link_text('64 bit Windows IE').click()

# 退出浏览器
time.sleep(100)
driver.quit()
