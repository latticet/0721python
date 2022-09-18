"""
异常传递：
异常传递就是异常如果没有被捕获，会一直向外抛出，知道程序结束没有被捕获，最终抛出异常信息。
"""


# TODO 函数嵌套
def fn1():
    1 / 0


def fn2():
    fn1()


def fn3():
    try:
        fn2()
    except ZeroDivisionError as e:
        print(e)


# fn3()

# TODO try嵌套
try:
    try:
        try:
            num = int(input('输入数字：'))
            result = num / 0
        except NameError:
            print('NameError')
    except ValueError:
        print('不能输入非数字')
except ZeroDivisionError as e:
    print(e)
