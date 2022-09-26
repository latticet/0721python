name = 'module1'


def fn():
    print('fn方法')


class Demo:
    pass


# __all__ 指定当前模块以import * 导入的时候，可以导入的资源
# 注意：列表中写的是资源名称的字符串形式
__all__ = ['name', 'fn']
