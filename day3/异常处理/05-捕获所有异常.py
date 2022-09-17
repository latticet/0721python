"""
语法:
try:
    可能发生异常的代码
except Exception [as e]:
    print(result)
"""

try:
    num = int(input('输入数字：'))
    result = num / 0
except Exception as e:
    print(e)



