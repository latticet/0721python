
# 装饰器
def decorator(fn):
    def inner(*args, **kwargs):
        print('正在运算中...')
        # 前置扩展功能
        result = fn(*args, **kwargs)
        # 后置扩展功能
        return result
    return inner


@decorator
def add1(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


@decorator
def add2(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5


@decorator
def add3(num1, num2, num3):
    return num1 + num2 + num3


if __name__ == '__main__':
    print(add1(1, 2, num3=3, num4=4))

    print(add2(1, 2, 3, 4, 5))

    print(add3(1, 2, 3))



