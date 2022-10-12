import os
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('https://www.itsource.cn/')
time.sleep(2)
# 测试操作：正常用户的操作
# close_element = driver.find_element_by_xpath('//*[@id="iframe_company_mini_div"]/h6/span[2]')
# close_element.click()
# javascript = ECMAScript + Bom + Dom
js = "div1 = document.getElementById('iframe_company_mini_div');div1.style.display='none'"
driver.execute_script(js)

time.sleep(50)
driver.quit()
