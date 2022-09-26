"""
受保护权限：面向对象思想里，只能在类的内部和派生来中访问受保护的成员，类的外部不能访问。但是在python语言中没有强制要求
受保护语法：在成员前加单下划线。
protected(受保护)
private(私有)
public(公有)
"""


class Person:
    def __init__(self):
        # 私有属性name
        self._name = 'hello'

    def _fn(self):
        """私有方法fn"""
        print('fn方法')


class Man(Person):
    def my_fn(self):
        print(self._name)


p1 = Person()
print(p1._name)
p1._fn()
