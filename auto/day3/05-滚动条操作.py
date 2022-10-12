import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.163.com')
driver.maximize_window()

# 滚动条操作
# 滚动条到浏览器的最底部
"""
js1 = 'window.scrollTo(0, document.body.scrollHeight)'
driver.execute_script(js1)
"""
js11 = 'window.scrollTo({top:document.body.scrollHeight, left:0, behavior:"smooth"})'
driver.execute_script(js11)

time.sleep(2)

# 滚动条到浏览器的最顶部
js2 = 'window.scrollTo(0, 0)'
driver.execute_script(js2)


time.sleep(10)
driver.quit()
