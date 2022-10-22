import time

from common.base import Base, By
from common.functions import open_browser


class CategoryPage(Base):
    """封装表现层: 制作定位器"""
    goods_list = (By.CSS_SELECTOR, '.goods-title>a')  # 定位页面中所有的商品
    goods_total = (By.CSS_SELECTOR, 'td.tdl>b')

    def get_goods_total_text(self):
        return self.get_element_text(self.goods_total)

    def get_goods_title(self):
        """
        获取商品标题
        :return: title
        """
        goods = self.find_elements(self.goods_list)  # 定位所有商品元素
        return [i.get_attribute('title') for i in goods]

    def click_goods(self, title):
        """点击所有商品"""
        goods_loc = ('css selector', f'a[title="{title}"]')  # 针对单个商品编写对应的定位器
        self.click(locator=goods_loc)


if __name__ == '__main__':
    driver = open_browser()
