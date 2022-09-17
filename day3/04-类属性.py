"""
类属性属于整个类
对象属性属于每个对象
"""
class Person:
    # 定义类属性
    country = '中国'


# 类的外部
# 语法：类名.类属性名
#      对象.类属性名

print(Person.country)
p1 = Person()
print(p1.country)

# 修改类属性
Person.country = 'China'
print(Person.country)
