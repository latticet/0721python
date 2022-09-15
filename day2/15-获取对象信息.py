# TODO ● type  查看数据类型
str1 = 'hello'
print(type(str1))


class Demo:
    def __init__(self):
        self.name = 'hello'
        self.age = 18

    def fn(self):
        pass


demo = Demo()
print(type(demo))
print('==' * 20)

# TODO ● dir  查看对象上所有方法和属性
print(dir(demo))
print(dir('hello'))

print('==' * 20)
# ● isinstance  查看对象是否属于某个类. True|False
print(isinstance('hello', str))
print(isinstance(demo, Demo))


class Demo2:
    pass


print(isinstance(demo, Demo2))
