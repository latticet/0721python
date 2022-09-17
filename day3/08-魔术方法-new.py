"""
作用:创建类的实例,并返回
触发:创建类的实例的时候
"""


class Demo(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


demo = Demo()  # None
demo = Demo()  # None
print(demo)

print('==' * 20)


# 函数（方法）返回None的三种情况
# 第一种
def fn1():
    print(None)


# 第二种
def fn2():
    return None


# 第三种
def fn3():
    return

# 调用
# print(fn1())
