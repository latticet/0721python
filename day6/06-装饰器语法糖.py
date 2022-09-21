# 装饰器定义
def wrapper(fn):
    def inner():
        print('扩展前置功能')
        fn()
        print('扩展后置功能')
    return inner


# 准备函数
# TODO 装饰器的语法糖方式
# 在要装饰函数的上面添加@装饰器名称
@wrapper
def fn():      # fn = wrapper(fn)
    print('fn')


# TODO 传统装饰方式
# 装饰函数
# wrapper装饰器装饰fn这个函数
# fn = wrapper(fn)


if __name__ == '__main__':
    fn()



