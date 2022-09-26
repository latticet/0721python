"""
需求1：创建2只猫，一只名字叫二狗， 另一只名字叫大狗， 大狗年龄5岁， 二狗年龄3岁
需求2：每只猫，说出自己的名字和年龄：我的名字是：xxx， 年龄是：xx

类名：Cat
属性：name age
方法：talk
"""


# 定义
class Cat:
    def __init__(self, name, age):
        # 初始化属性
        self.name = name
        self.age = age

    def talk(self):
        print(f'我的名字是：{self.name}， 年龄是：{self.age}')


# 调用
cat1 = Cat('大狗', 5)
cat1.talk()

cat2 = Cat('二狗', 3)
cat2.talk()
