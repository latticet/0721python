class Person:
    # 定义类属性
    country = '中国'

    def __init__(self):
        self.name = 'hello'
        self.age = 18

    @classmethod  # 语法形式叫做装饰器
    def get_country(cls):
        # 类方法
        # cls： 当前类
        print(cls)
        return cls.country

    def set_age(self, age):
        """对象方法"""
        self.age = age


print(Person)
Person.get_country()

"""
如果不知道定义为什么方法，就定义为对象方法。
如果这个方法中用到类属性，那么就定义为类方法
如果这个方法中用到对象属性，那么就定义为对象方法。
如果这个方法中，既用不到对象属性，也用不到类属性。那么就定义为静态方法
"""
