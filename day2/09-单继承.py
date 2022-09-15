"""
一个类只继承一个父类
动物类
狗类
"""


# 动物类
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def call(self):
        print('旺旺叫')

    def run(self):
        print('跑...')


# 狗类
class Dog(Animal):
    pass


# 调用
dog = Dog('恭喜发财', 3, 'blue')
print(dog.name)
print(dog.age)
print(dog.color)
