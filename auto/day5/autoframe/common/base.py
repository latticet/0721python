"""
对selenium进行二次封装
Base:
    初始化浏览器驱动对象
    退出浏览器
    元素定位
    请求目标网址
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 打开浏览器，获取浏览器驱动
def get_driver(browser='chrome'):
    if browser == 'chrome':
        # chrome浏览器驱动
        return webdriver.Chrome()
    else:
        # firefox浏览器驱动
        return webdriver.Firefox()


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        """请求目标网址"""
        self.driver.get(url)
        # 浏览器最大化
        self.driver.maximize_window()

    def find_element(self, locator, timeout=5, poll_frequency=0.5):
        """
        定位单个元素
        :param locator: 定位器
        :param timeout: 超时时间
        :param poll_frequency: 间隔时间
        :return: WebElement对象|None
        """
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency) \
                .until(EC.presence_of_element_located(locator), message='元素定位失败')
        except TimeoutException as e:
            print(e)
            return None

    def find_elements(self, locator, timeout=5, poll_frequency=0.5):
        """定位多个元素"""
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency) \
                .until(EC.presence_of_all_elements_located(locator), message='元素定位失败')
        except TimeoutException as e:
            print(e)
            return []


if __name__ == '__main__':
    driver = get_driver()
    base = Base(driver)
    base.get('https://www.baidu.com')
    # print(base.find_element((By.ID, 'su'), timeout=1))
    print(len(base.find_elements((By.TAG_NAME, 'input'), timeout=1)))
