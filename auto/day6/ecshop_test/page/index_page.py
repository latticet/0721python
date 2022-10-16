import time

from common.base import Base, get_driver
from selenium.webdriver.common.by import By


class IndexPage(Base):
    def font_username_text(self):
        return self.get_text((By.XPATH, '//font[@class="f4_b"]'))

    def a_logout(self):
        self.click((By.LINK_TEXT, '退出'))

    def a_login(self):
        self.click((By.PARTIAL_LINK_TEXT, '请登录'))
