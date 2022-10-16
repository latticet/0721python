import unittest
import ddt


@ddt.ddt
class DemoTestCase(unittest.TestCase):
    # 测试数据
    data_list = [
        'hello',
        'good'
    ]

    @ddt.data(*data_list)
    def test_login(self, item):
        print(item)


if __name__ == '__main__':
    unittest.main(verbosity=2)
