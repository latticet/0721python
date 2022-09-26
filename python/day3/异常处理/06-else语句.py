"""
语法：
try:
    可能发生异常的代码
except Exception as result:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
"""
try:
    num = int(input('输入数字：'))
except ZeroDivisionError:
    print('0不是是除数')
except ValueError:
    print('必须输入数字')
else:
    print("没有抛出异常")
