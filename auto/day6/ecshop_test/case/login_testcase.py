import unittest
from common.base import get_driver
from page.login_page import LoginPage
from page.index_page import IndexPage


class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 创建浏览器对象，打开浏览器
        driver = get_driver()
        # 请求测试网址
        driver.get(LoginPage.login_url)
        cls.login = LoginPage(driver)
        cls.index = IndexPage(driver)

    def test_01_login(self):
        # TODO 操作流程'
        expect_username = 'fine1'
        # 输入用户名
        self.login.input_username(expect_username)
        # 输入密 码
        self.login.input_password('123456')
        # 点击登 录
        self.login.input_submit()

        # TODO 断言
        # 预期 和 实际结果的比对
        # fine1 和 获取实际结果
        # 定位预期结果
        actual_username = self.index.font_username_text()
        self.assertEqual(expect_username, actual_username, msg='断言登录成功')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
