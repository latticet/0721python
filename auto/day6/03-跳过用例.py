import unittest

gender = input('性别【男|女】：')


class DemoTestCase(unittest.TestCase):
    @unittest.skip(reason='无条件跳过')
    def test01(self):
        print('test01')

    # 条件成立跳过
    @unittest.skipIf(gender == '男', reason='男生跳过测试')
    def test02(self):
        print('test02')

    # 条件不成立跳过
    @unittest.skipUnless(gender == '男', reason='不是男跳过测试')
    def test03(self):
        print('test03')

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(1, 1, msg='断言1等于1')

    @unittest.expectedFailure
    def test05(self):
        self.assertEqual(1, 2, msg='断言1等于2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
