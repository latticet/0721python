# TODO 浅拷贝
# copy.copy(拷贝的数据)
# 可变数据类型
import copy
# 只拷贝最外层的对象
list1 = [1, 2, ['a', 'b']]
list2 = copy.copy(list1)
"""
print(f'list1:{id(list1)}, list1[2]:{id(list1[2])}')
print(f'list2:{id(list2)}, list2[2]:{id(list2[2])}')
"""
# 不可变数据类型
str1 = 'hello'
str2 = copy.copy(str1)
"""
print(f'str1:{id(str1)}')
print(f'str2:{id(str2)}')
"""

# TODO 深拷贝
# copy.deepcopy(拷贝的数据)
# 整体拷贝
# 可变数据类型
list1 = [1, 2, ['a', 'b', ['hello', 'good']]]
list2 = copy.deepcopy(list1)
print(f'list1:{id(list1)}, list1[2]:{id(list1[2])}, list1[2][2]:{id(list1[2][2])}')
print(f'list2:{id(list2)}, list2[2]:{id(list2[2])}, list2[2][2]:{id(list2[2][2])}')

# 不可变数据类型
str1 = 'hello'
str2 = copy.deepcopy(str1)
print(f'str1:{id(str1)}')
print(f'str2:{id(str2)}')



