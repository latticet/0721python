"""
装饰器就是一个特殊的闭包
特殊点：
    1. 外部函数要传入一个函数
    2. 内部函数调用传入的这个函数
作用：
    不改源代码， 不改调用方式，为函数添加额外的功能
"""


# 装饰器定义
def wrapper(fn):   # fn = demo
    def inner():
        print(123)
        fn()
        print(456)
    return inner


def demo():
    print('fn函数执行')


# 装饰器使用
# 需求
demo = wrapper(demo)   # demo = inner
demo()

