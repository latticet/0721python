import unittest


class DemoTestCase(unittest.TestCase):

    def test02(self):
        print('test02')

    def test01(self):
        print('test01')

    def testb(self):
        print('testb')

    def testa(self):
        print('testa')

    def mytest(self):
        print('mytest')


if __name__ == '__main__':
    unittest.main(verbosity=2)
