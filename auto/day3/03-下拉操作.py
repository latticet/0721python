import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/selectTest.htm')
        time.sleep(2)

    def select1(self):
        """普通下拉操作"""
        self.driver.find_element_by_xpath('//option[@value=48]').click()

    def select2(self):
        """select类方式"""
        # 定位要操作的select标签
        s1 = self.driver.find_element_by_id('s1')
        # 创建select对象
        select = Select(s1)

        # select.select_by_index()  # 通过索引选取option, 索引从0开始
        # Mail
        select.select_by_index(6)
        time.sleep(1)

        # select.select_by_value()  # 通过value值选取option
        select.select_by_value('49')
        time.sleep(1)

        # select.select_by_visible_text()  # 通过文本选取option
        select.select_by_visible_text('Email')

    def quit(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.select1()
    case.select2()
    case.quit()
