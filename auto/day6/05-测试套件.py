import unittest


class Demo1TestCase(unittest.TestCase):
    def test_1(self):
        print('test1')

    def test_2(self):
        print('test2')


class Demo2TestCase(unittest.TestCase):
    def test_a(self):
        print('testa')

    def test_b(self):
        print('testb')


if __name__ == '__main__':
    # TODO 创建测试套件
    suite = unittest.TestSuite()

    # suite.addTest：单个收集测试用例方法
    """
    suite.addTest(Demo1TestCase('test_2'))
    suite.addTest(Demo1TestCase('test_1'))
    suite.addTest(Demo2TestCase('test_b'))
    """

    # suite。addTests：批量收集测试用例方法
    tests = [
        Demo1TestCase('test_2'),
        Demo1TestCase('test_1'),
        Demo2TestCase('test_b')
    ]

    suite.addTests(tests)

    # TODO 创建执行器
    # 执行器只会执行套件收集的用例
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
