"""
可以去除传入的字符串里面的所有空格，返回去除空格之后的字符串
"""


def remove_space():
    string = input('输入字符串：')
    return string.replace(' ', '')


print(remove_space())
