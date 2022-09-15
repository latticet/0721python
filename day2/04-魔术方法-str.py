"""
魔术方法:__str__
触发机制: 当对象被print打印的时候,触发str方法执行
使用注意: str方法必须返回字符串类型
作用: 默认print打印对象,输出的是对象的地址.通过str方法可以返回自定义的一个字符串
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


p1 = Person('hello1')
print(p1)   # 这个时候回触发str魔术方法执行


p2 = Person('hello2')
print(p2)   # 这个时候回触发str魔术方法执行

