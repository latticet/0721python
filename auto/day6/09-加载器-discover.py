import unittest
from case import demo1_testcase

# 创建加载器
loader = unittest.TestLoader()

# loader.discover(start_dir, pattern='*_testcase')   通过目录路径加载
# TODO 通过目录路径加载
suite = loader.discover('case', pattern='*_testcase.py')

# 执行
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
