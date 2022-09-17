"""
新建一个文件，定义一个猫类，创建一个猫对象，调用上面的属性和方法
Cat:
    属性：name  age
    方法：run   eat
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}在跑步')

    def eat(self):
        print(f'{self.name}在吃东西')


cat = Cat('hello', 3)
cat.eat()
cat.run()
