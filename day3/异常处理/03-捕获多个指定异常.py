"""
语法：
# 第一种
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    捕获异常执行的代码


# 第二种
try:
    可能发生异常的代码
except 异常类型1:
    发生异常1,执行的代码
except 异常类型2:
    发生异常2,执行的代码
except ...:
    pass
"""

# TODO 第一种
"""
try:
    num = int(input('输入数字：'))
    result = num / 0
except (ValueError, ZeroDivisionError):
    print('发生异常')
"""

# TODO 第二种
try:
    num = int(input('输入数字：'))
    result = num / 0
except ValueError:
    print('不能传入非数字')
except ZeroDivisionError:
    print('0不能是除数')
