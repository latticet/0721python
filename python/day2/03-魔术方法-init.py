"""
魔术方法：__init__
触发：当类的实例创建以后，自动执行__init__方法
作用：用例初始化对象的属性
说明：这个魔术方法是最重要，使用最多的，以后我们设置对象属性一般都在这个方法里面设置
"""


class Person:
    def __init__(self, name, age):
        # print('init执行了')
        # 初始化对象属性
        print(self)
        self.name = name
        self.age = age


p1 = Person('陈雅琪', 18)
# print(f'p1:{p1}')
print(p1.name)
print(p1.age)

print('==' * 20)

p2 = Person('卢佳悦', 17)
print(p2.name)
print(p2.age)
# print(f'p2:{p2}')
