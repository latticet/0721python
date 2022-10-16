import unittest


class DemoTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, 1, msg='断言1和1相等')

    def test02(self):
        self.assertEqual(1, 2, msg='断言1和2相等')

    def test03(self):
        self.assertNotEqual(1, 3, msg='断言1和3不相等')


if __name__ == '__main__':
    unittest.main(verbosity=2)
