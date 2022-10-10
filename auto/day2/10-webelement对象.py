"""
8个定位元素方法正常返回的那个对象就是WebElement对象
"""
import os
import time

from selenium import webdriver


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def attr(self):
        """属性"""
        self.driver.get('https://www.baidu.com')

        # kw
        kw = self.driver.find_element_by_id('kw')
        # print(kw.id)
        # print(kw.size)
        # print(kw.rect)
        news = self.driver.find_element_by_link_text('新闻')
        # print(news.text)
        # print(kw.tag_name)

    def fn1(self):
        """方法"""
        self.driver.get('https://www.baidu.com')
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('天气预报')
        time.sleep(2)
        kw.clear()

        # TODO 重点
        print(kw.get_attribute('outerHTML'))
        print(kw.get_attribute('id'))
        print(kw.get_attribute('class'))
        print(kw.get_attribute('name'))

    def fn2(self):
        """方法"""
        url = os.path.join(os.path.abspath('html'), 'demo2.html')
        self.driver.get(url)

        # 定位div1
        div1 = self.driver.find_element_by_id('div1')
        # 定位div2
        div2 = self.driver.find_element_by_id('div2')

        print(div1.is_displayed())
        print(div2.is_displayed())

        ipt1 = self.driver.find_element_by_xpath('//input[1]')
        ipt2 = self.driver.find_element_by_xpath('//input[2]')
        print(ipt1.is_enabled())
        print(ipt2.is_enabled())


    def quit(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.attr()
    # case.fn1()
    case.fn2()
    case.quit()
