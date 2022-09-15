"""
魔术方法:__del__
触发机制：当对象被销毁以后执行这个方法   del obj， 当脚本执行完毕以后，所有的数据都会自动销毁
作用：在对象被销毁以后可以做一些销毁之后的收尾工作
"""


class Person:
    def __del__(self):
        print('del执行了')


p1 = Person()
# del p1