"""
将selenium案例转化为面向对象版本，添加360搜索
类名：TestCase
    方法：
        init: 打开浏览器
        baidu：百度的逻辑
        so360：360的逻辑
        quit: 退出浏览器
"""
from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def baidu(self):
        """百度的逻辑"""
        # 请求百度网址
        self.driver.get('https://www.baidu.com')
        time.sleep(1)
        # 搜索框输入关键字
        self.driver.find_element_by_id('kw').send_keys('天气预报')
        time.sleep(1)
        # 点击百度一下搜索
        self.driver.find_element_by_id('su').click()

    def so360(self):
        """360的逻辑"""
        # 请求360搜索
        self.driver.get('https://www.so.com')
        # 搜索框输入关键字
        self.driver.find_element_by_id('input').send_keys('天气预报')
        # 点击搜索一下搜索
        self.driver.find_element_by_id('search-button').click()

    def quit(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.baidu()
    case.so360()
    case.quit()
