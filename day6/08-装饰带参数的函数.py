
# 定义装饰器
def decorator(fn):
    def inner(num1, num2):
        print('正在运算中...')
        return fn(num1, num2)
    return inner


#  定义函数
# 需求： 求2个数的和
@decorator
def add(num1, num2):
    return num1 + num2


@decorator
def subtraction(num1, num2):
    return num1 - num2


if __name__ == '__main__':
    result = add(1, 2)
    print(result)

    print(subtraction(2, 1))

