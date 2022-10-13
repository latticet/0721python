from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器，请求目标网址
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# WebDriverWait(driver,10).until(method，message="")
# WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道1'), message='我的异常描述信息')


# 显示等待方式定位标签
locator = ('id', 'kw1')
kw_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator), message='定位不到元素')
print(kw_element.get_attribute('outerHTML'))

# 退出浏览器
driver.quit()