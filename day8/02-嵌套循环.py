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

print('==' * 20)
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

print('==' * 20)
# 第三个需求
# 实现99乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {j * i}', end='\t')
        j += 1
    print()
    i += 1

# for循环99乘法表
print('==' * 20)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {j * i}', end='\t')
    print()


# dict
dict1 = {'name':'hello', 'age':18}
for key, value in dict1.items():
    print(key, value)
