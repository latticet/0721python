import time

from common.base import Base, get_driver
from selenium.webdriver.common.by import By


class IndexPage(Base):
    def font_username_text(self):
        return self.get_text((By.XPATH, '//font[@class="f4_b"]'))
