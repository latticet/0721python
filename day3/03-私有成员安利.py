"""
Person类
 属性：name age
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        # 私有成员
        self.__age = age

    def set_age(self, age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print('年龄不合法')

    def get_age(self):
        return self.__age


p1 = Person('hello', 18)
# print(p1.name)
# print(p1.age)
# 访问私有成员 _类名__私有成员名称
print(p1._Person__age)

# p1.set_age(10000)
# print(p1.get_age())
