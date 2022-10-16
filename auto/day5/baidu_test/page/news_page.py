"""
新闻页面测试需要用的标签操作：
1. 搜索框输入内容
2. 百度一下点击
3. 第一个超链接点击一下
"""
import time

from common.base import Base, get_driver
from selenium.webdriver.common.by import By


class NewsPage(Base):
    def input_word(self, content):
        self.send_keys((By.ID, 'ww'), content)

    def input_button(self):
        self.click((By.ID, 's_btn_wr'))

    def a_click(self):
        self.click((By.XPATH, '//div[@id="pane-news"]//a'))


if __name__ == '__main__':
    news = NewsPage(get_driver())
    news.get('https://news.baidu.com')
    news.input_word('天气预报')
    time.sleep(1)
    news.input_button()
    time.sleep(1)
    news.driver.back()
    time.sleep(1)
    news.a_click()
    news.quit()
