# 可变数据类型
list1 = [1, 2, 3]
list2 = list1

# 列表末尾追加1个4
list1.append(4)
# 列表头部添加1个0
list1.insert(0, 0)

print(list1)
print(list2)

# 不可数据类型
str1 = 'hello'
str2 = 'hello'

print(id(str1))
print(id(str2))




