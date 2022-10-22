import unittest

import ddt

from common.functions import open_browser
from page.reception.index_page import IndexPage
from page.reception.login_page import LoginPage
from common.data_operation import DataOperation

data = DataOperation('user_info.csv')
user_data = data.get_data_to_dict()


@ddt.ddt
class LoginTestCase(unittest.TestCase):
    user_data = user_data

    @classmethod
    def setUpClass(cls) -> None:
        # 创建浏览器对象，打开浏览器
        driver = open_browser()
        # 请求测试网址
        driver.get(LoginPage.login_url)
        cls.login = LoginPage(driver)
        cls.index = IndexPage(driver)

    @ddt.data(*user_data)
    def test_login(self, userinfo):
        # TODO 操作流程'
        expect_username = userinfo['username']
        # 输入用户名
        self.login.input_username(expect_username)
        # 输入密 码
        self.login.input_password(userinfo['password'])
        # 点击登 录
        self.login.input_submit()

        # TODO 断言
        # 预期 和 实际结果的比对
        # 定位实际结果
        actual_username = self.index.font_username_text()
        if userinfo['title'] == 'ok':
            self.assertEqual(expect_username, actual_username, msg=userinfo['title'])
        else:
            self.assertNotEqual(expect_username, actual_username, msg=userinfo['title'])

    def tearDown(self) -> None:
        self.index.a_logout()
        self.index.a_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
