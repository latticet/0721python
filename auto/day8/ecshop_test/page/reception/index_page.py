import time

from common.base import Base, By
from common.functions import host, open_browser


class IndexPage(Base):
    index_url = host

    """封装表现层: 制作定位器"""
    category_locator = ('css selector', '.cat-box>.cat1>a')  # 定位页面中所有的商品

    def category_url_list(self):
        return [a_element.get_attribute('href') for a_element in self.find_elements(locator=self.category_locator)]

    def font_username_text(self):
        return self.get_text((By.XPATH, '//font[@class="f4_b"]'))

    def a_logout(self):
        self.click((By.LINK_TEXT, '退出'))

    def a_login(self):
        self.click((By.PARTIAL_LINK_TEXT, '请登录'))


if __name__ == '__main__':
    driver = open_browser()
    index = IndexPage(driver)
    index.get(index.index_url)
    print(index.category_url_list())
