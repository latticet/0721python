# 定义类
class Person:
    # 类的内部
    pass


# 类的外部 - 对象属性操作
# 创建对象
p1 = Person()

# TODO 设置
# 语法： 对象.属性名 = 属性值
p1.name = '郑善文'
p1.age = 18

# TODO 获取
# 语法：对象.属性名
print(f'名字是：{p1.name}')
print(f'年龄是：{p1.age}')

# TODO 修改
# 语法：对象.属性名 = 新的值
p1.name = '李杨'
p1.age = 19
print('==' * 20)
print(p1.name, p1.age)

# TODO 删除
# 语法（通用语法）：del p1.name
del p1.name
print(p1.name)
