# 单个异常情况
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)

print('==' * 20)

# 多个异常情况
try:
    num = int(input('输入数字：'))
    result = num / 0
except (ValueError, ZeroDivisionError) as e:
    print(e)
