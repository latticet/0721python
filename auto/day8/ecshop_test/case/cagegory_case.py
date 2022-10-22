import unittest
import ddt
from common.functions import open_browser
from page.reception.index_page import IndexPage
from page.reception.category_page import CategoryPage
from page.reception.goods_page import GoodsPage

# 频道数据
driver = open_browser()
index = IndexPage(driver)
index.get(index.index_url)
channel = index.category_url_list()


@ddt.ddt
class GoodsListTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = index
        cls.category = CategoryPage(driver)
        cls.goods = GoodsPage(driver)

    @ddt.data(*channel)
    def test_channel(self, channel_url):
        # 请求频道网址
        self.index.get(channel_url)
        # 获取当前频道商品数量
        goods_total = self.category.get_goods_total_text()
        if int(goods_total):
            # 获取当前频道所有商品标题
            goods_titles = self.category.get_goods_title()
            # 通过商品标题定位商品，执行点击
            for title in goods_titles:
                self.category.click_goods(title)
                goods_title = self.goods.get_goods_title_text()
                self.assertEqual(title.strip(), goods_title)
                self.goods.back()

    def tearDown(self) -> None:
        self.category.back()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.index.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
