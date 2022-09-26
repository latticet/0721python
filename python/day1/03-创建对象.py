"""
创建对象
语法：
类名()
"""


# 定义Person类
class Person:
    pass


# 创建Person类的对象(类的实例)
p1 = Person()
# <__main__.Person object at 0x7fdfbab85a30>
# Person类的实例， 在【0x7fdfbab85a30】这个内存地址中
"""
# 关于对象的内存地址
print(p1)  # 16进制
print(hex(id(p1)))  # 10进制转化为16进制
print(id(p1))  # 10进制
"""

# 一个类可以创建多个对象
p2 = Person()
p3 = Person()

# 输出不同对象的内存地址，验证对象之间是隔离的。
print(p1)
print(p2)
print(p3)
