import time

from common.base import Base, By


class GoodsPage(Base):
    def get_goods_title_text(self):
        locator = (By.CSS_SELECTOR, 'div.goods_style_name')
        return self.get_element_text(locator) if self.get_element_text(locator) else self.get_element_text(locator)
