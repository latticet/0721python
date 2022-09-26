# 定义装饰器
def wrapper(fn):   # fn = demo
    def inner():
        print('前置操作')
        result = fn()   # 2
        print('后置操作')
        return result

    return inner


# 定义函数
@wrapper
def demo():    # demo = inner
    return 1 + 1


print(demo())   # inner()




