import time

from selenium.common.exceptions import InvalidArgumentException, WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.functions import open_browser


class Base:
    """
    基础类,封装了selenium基础方法,供page包下面的类继承
    """

    def __init__(self, driver):
        # 设置driver
        self.driver = driver
        self.driver.maximize_window()

    def get(self, url):
        # 请求目标网址
        try:
            self.driver.get(url)
        except (InvalidArgumentException, WebDriverException):
            print('输入的地址不正确')

    def find_element(self, locator, timeout=1):  # locator = (By.xxx, value)
        # 定位元素, 返回元素
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator), '定位失败')
        except TimeoutException:
            print(f'{locator}定位失败')

    def find_elements(self, locator, timeout=1):
        # 定位元素, 返回元素列表
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator), '定位失败')
        except TimeoutException:
            print(f'{locator}定位失败')

    def click(self, locator):
        # 元素点击操作
        element = self.find_element(locator)
        if element:
            element.click()

    def get_attribute(self, locator, attr):
        # 获取元素属性
        element = self.find_element(locator)
        if element:
            return element.get_attribute(attr)  # 返回正确的属性值, 获取不到就返回None

    def get_element_text(self, locator):
        # 获取元素文本
        element = self.find_element(locator)
        if element:
            return element.text

    def implicitly_wait(self, seconds=5):
        # 隐式等待
        self.driver.implicitly_wait(seconds)

    def send_keys(self, locator, content):
        # 输入内容
        self.find_element(locator).send_keys(content)

    def get_text(self, locator):
        element = self.find_element(locator)
        if element:
            return element.text

    def quit(self, seconds=0):
        # 退出浏览器
        time.sleep(seconds)
        self.driver.quit()

    def back(self):
        self.driver.back()


if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    base.get('https://www.baidu.com')

    print(base.get_attribute((By.ID, 'kw'), 'outerHTML'))
    print(base.get_attribute((By.ID, 'kw'), 'name'))
    print(base.get_attribute((By.ID, 'kw'), 'abc'))

    base.quit(2)
