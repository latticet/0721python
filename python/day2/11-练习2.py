"""
员工类
 属性：姓名， 年龄
 方法：跑步， 吃饭
讲师类（员工类）
 方法：讲课
班主任类（员工类）
"""


# 员工类
class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('跑步')

    def eat(self):
        print('吃饭')


# 讲师类
class Teacher(Staff):
    def teach(self):
        print('讲课')


# 班主任类
class HeadMaster(Staff):
    pass
