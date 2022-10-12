import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        time.sleep(2)

    def click(self):
        time.sleep(2)
        # 简易操作
        # web_element.click()
        """
        self.driver.find_element_by_xpath('//input[@value="click me"]').click()
        """

        # TODO AC对象操作
        # 创建ac对象
        ac = ActionChains(self.driver)
        # 要操作的标签对象
        ipt = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ac.click(ipt).perform()

    def context_click(self):
        """右击"""
        # 创建ac对象
        ac = ActionChains(self.driver)
        # ac对象的操作方法, perform执行
        ipt = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        ac.context_click(ipt).perform()

    def double_click(self):
        """双击"""
        # 创建ac对象
        ac = ActionChains(self.driver)
        # ac对象的操作方法, perform执行
        ipt = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ac.double_click(ipt).perform()

    def drag_and_drop(self):
        """拖动"""
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        time.sleep(1)

        # 创建ac对象
        ac = ActionChains(self.driver)
        # ac对象的操作方法, perform执行
        source = self.driver.find_element_by_id('dragger')
        target = self.driver.find_element_by_xpath('//div[4]')

        ac.drag_and_drop(source, target).perform()

    def move_to_element(self):
        """鼠标悬停"""
        self.driver.get('https://sahitest.com/demo/mouseover.htm')
        time.sleep(1)

        # 创建ac对象
        ac = ActionChains(self.driver)
        # ac对象的操作方法, perform执行
        div = self.driver.find_element_by_xpath('//div/div')
        ac.move_to_element(div).perform()

    def click_and_hold(self):
        """鼠标长按"""
        url = os.path.join(os.path.abspath('html'), 'mouse_hold.html')
        self.driver.get(url)
        time.sleep(1)

        ac = ActionChains(self.driver)
        btn = self.driver.find_element_by_id('btn1')
        ac.click_and_hold(btn).perform()

    def quit(self, seconds=2):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.click()
    # case.context_click()
    # case.double_click()
    # case.drag_and_drop()
    # case.move_to_element()
    case.click_and_hold()
    case.quit()
