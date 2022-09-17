"""
多态实现：
1. 有继承关系
2. 子类重写父类的方法
3. 定义一个接口融统一调用这个方法
"""


class Animal:
    def call(self):
        print('动物叫')


class Cat(Animal):
    def call(self):
        print('喵喵叫')


class Dog(Animal):
    def call(self):
        print('旺旺叫')


class Person(Animal):
    pass


def do_call(obj):  # object
    # 开始时间
    obj.call()
    # 结束时间
    # 运行时间 = 结束时间 - 开始时间


# 调用
do_call(Dog())
do_call(Cat())
do_call(Person())
