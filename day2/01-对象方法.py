"""
关于对象方法：
1. 在类的内部定义
2. 和函数的定义方式相同
3. 特殊：必须要有第一个参数，名字一般我们都写self
"""


class Person:
    # 类的内部
    # TODO 定义对象方法
    def run(self):
        print(self)


# 类的外部
# TODO 调用对象方法
# 语法： obj.fn()
# 说明： 方法名前面要加上对象，其他使用和函数相同
p1 = Person()
# p1.run()

# TODO self说明
# 1.self是什么
# self是调用当前方法的对象
print(p1)
p1.run()
print('==' * 20)
p2 = Person()
print(p2)
p2.run()

# 2.为什么self形参，在调用方法的时候不需要传入实参
# 原因是：对象方法在调用的时候，python解释器会自动把对象方法前面的对象自动传入到方法的第一个参数self
