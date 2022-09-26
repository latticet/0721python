import random
# random.random()	实数相关	用于生成一个0到1的随机浮点数: [0, 1)
"""
print(random.random())
"""

# random.uniform(a,b)		生成[a,b]或[b,a]之间的均匀分布随机浮点数。
"""
for i in range(3):
    print(random.uniform(1, 10))
"""

# random.randint(a,b)	整数相关	生成[a,b]的随机整数，要求a < b。
"""
for i in range(3):
    print(random.randint(1, 10))

# 案例：随机生成6位的验证码
code = '%06d' % random.randint(1, 999999)
print(code)
# 字符串格式化
# f-sring
# %格式化 %06d %f %s
# string.format()
"""

# random.randrange(a,b)		生成[a,b)的随机整数，第三个参数可以指定步长。
"""
print(random.randrange(1, 10, 2))
"""
# random.choice(seq)	    序列相关	从序列中随机选择一个元素，若序列为空，则抛出异常。
# 序列：列表，元组，字符串
"""
print(random.choice(['python', 'mysql', 'git', 'linux']))
print(random.choice(('apple', 'orange')))
print(random.choice('hello'))
"""

# random.shuffle(seq)		打乱原序列，原序列必须可写。
"""
list1 = ['python', 'mysql', 'git', 'linux']
random.shuffle(list1)
print(list1)
"""

# random.sample(seq,k)		从序列中随机选择k个元素返回，原序列不变。
"""
list1 = ['python', 'mysql', 'git', 'linux']
print(random.sample(list1, 2))
print(random.sample(list1, 3))
"""

# random.seed(n=none)	初始化	初始化随机熵池。
"""
random.seed(1)
print(random.randint(1, 10))

random.seed(2)
list1 = ['python', 'mysql', 'git', 'linux']
print(random.sample(list1, 2))
"""