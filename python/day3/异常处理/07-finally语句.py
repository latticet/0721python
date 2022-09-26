"""
语法：
# 异常的完整格式
try:
    可能发生异常的代码
except 异常类型:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
finally:
    无论是否异常都要执行的代码
"""

try:
    f = open('resource/demo.txt', encoding='utf8')
except FileNotFoundError:
    f = open('resource/demo.txt', mode='w', encoding='utf8')
    f.write('123\n456')
else:
    content = f.read()
    print(content)
finally:
    f.close()
