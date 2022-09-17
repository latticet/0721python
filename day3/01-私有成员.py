"""
私有成员：具有私有权限的属性和方法
私有权限：只能在类的内部访问
私有权限语法：
在属性名或者方法名的前面加双下划线。比如：
__name
__fn
"""


class Person:
    def __init__(self):
        # 私有属性name
        self.__name = 'hello'

    def __fn(self):
        """私有方法fn"""
        print('fn方法')


class Man(Person):
    pass


p1 = Person()
print(p1.__name)
p1.__fn()

"""
m1 = Man()
print(m1.name)
m1.fn()
"""
