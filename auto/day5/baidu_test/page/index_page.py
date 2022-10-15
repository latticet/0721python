"""
测试项目中的一个页面，对应这里的一个模块
首页：index_page模块
一个模块中定义一个类
类中封装操作方法
"""
from common.base import Base, get_driver
from selenium.webdriver.common.by import By


class IndexPage(Base):
    def input_send_keys(self, keyword):
        self.send_keys((By.ID, 'kw'), keyword)

    def input_click(self):
        self.click((By.ID, 'su'))


if __name__ == '__main__':
    # 创建浏览器驱动
    driver = get_driver()
    index = IndexPage(driver)
    # 访问目标网址
    index.get('https://www.baidu.com')
    index.input_send_keys('天气预报')
    index.input_click()

    index.quit(2)
