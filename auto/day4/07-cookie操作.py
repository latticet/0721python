from selenium import webdriver
from pprint import pprint

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')


# driver.get_cookies()	获得所有cookie 信息
# pprint(driver.get_cookies())

# driver.get_cookie(name)	返回特定name 的cookie 信息
# print(driver.get_cookie('ZFY'))

# driver.add_cookie(cookie_dict)	添加cookie，必须有name 和value 值
driver.add_cookie({'name':'selenium', 'value':'selenium练习'})
print(len(driver.get_cookies()))

# driver.delete_cookie(name)	删除特定(部分)的cookie 信息
driver.delete_cookie('selenium')
print(len(driver.get_cookies()))

# driver.delete_all_cookies()	删除所有cookie 信息
driver.delete_all_cookies()
print(len(driver.get_cookies()))


driver.quit()