import time

import selenium.webdriver


class TestCase:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def set_window(self):
        """设置窗口大小"""
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.set_window_size(500, 800)
        time.sleep(1)
        self.driver.minimize_window()

    def forward_back(self):
        """前进后退"""
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.forward()

    def quit(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.forward_back()
    case.set_window()
    case.quit()
