import unittest
from HTMLTestRunner import HTMLTestRunner

# 收集测试用例
# 创建加载器
loader = unittest.TestLoader()
suite = loader.discover('case', pattern='*_testcase.py')

with open('report/ecshop_report.html', 'wb') as f:
    # 执行测试报告
    # 把测试结果写入到文件中
    runner = HTMLTestRunner(
        title='ecshop的测试报告',
        description='测试报告描述',
        tester='测试报告作者',
        verbosity=2,
        stream=f  # 要写如文件的资源句柄
    )
    # 执行测试用例
    runner.run(suite)
