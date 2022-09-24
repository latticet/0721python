# 第一个需求
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

j = 1
while j < 6:
    i = 1
    while i < 6:
        print('*', end=' ')
        i += 1
    print()
    j += 1

print('=='*20)
# 第二个需求
"""
*
* *
* * * 
* * * *
* * * * *
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

print('=='*20)
# 第三个需求
# 实现99乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {j*i}', end='\t')
        j += 1
    print()
    i += 1

