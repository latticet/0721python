# 定义商品类
class Goods:
    def __init__(self):
        self.name = '商品'

    def fn(self):
        print('商品的fn方法')


# 定义手机类
class Phone(Goods):
    def __init__(self):
        self.name = '手机'

    def fn(self):
        print('手机的fn方法')


p1 = Phone()
print(p1.name)
p1.fn()
