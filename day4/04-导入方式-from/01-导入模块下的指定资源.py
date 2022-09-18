"""
# 导入模块下的指定资源
from 模块名 import 资源名1 [as 别名], 资源名2, ...
"""
from module1 import name as m_name, fn, Demo

name = '当前模块的name'

print(name)
print(m_name)
fn()
print(Demo())
