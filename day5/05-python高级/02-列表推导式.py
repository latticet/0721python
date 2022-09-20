# 需求： 1- 100的列表
# 传统 左闭右开区间
list1 = []
for i in range(1, 101):
    list1.append(i)

# print(list1)

# TODO 列表推导式
# 特点：语法简单，效率高
# 语法： [生成元素的表达式 控制元素生成个数的表达式]
list2 = [i for i in range(1, 101)]
# print(list2)

# TODO 案例
# 需求：生成1-100的奇数列表
# 第一种
list3 = [i for i in range(1, 101, 2)]
# print(list3)

# 第二种
# 传统
list4_1 = []
for i in range(1, 101):
    if i % 2 != 0:
        list4_1.append(i)
# print(list4_1)
# 列表推导式
list4_2 = [i for i in range(1, 101) if i % 2 != 0]
# print(list4_2)

# 需求：列表里面有10个helloworld  ['helloworld', 'helloworld', ...]
list5 = ['helloworld' for i in range(10)]
print(list5)


list6 = ['helloworld' + str(i) for i in range(10)]
# print(list6)

# 需求：[(1, 1), (1, 2), (2,1), (2,2)]
# 传统方式
list7_1 = []
for i in range(1, 3):
    for j in range(1, 3):
        list7_1.append((i, j))
# print(list7_1)

# 列表推导式
list7_2 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list7_2)














