"""
使用装饰器完成对下面函数运行时间的计算
"""
import time


# 装饰器定义
def decorator(fn):
    def inner(*args, **kwargs):
        # 开始时间
        start = time.time()
        result = fn()
        # 结束时间
        end = time.time()
        # 结束时间 - 开始时间
        print(end - start)
        return result

    return inner


# 函数1
@decorator
def demo1():
    for i in range(100000000):
        pass


# 函数2
@decorator
def demo2():
    for i in range(100000):
        pass


if __name__ == '__main__':
    demo1()
    demo2()
