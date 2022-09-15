# 定义商品类
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def fn(self):
        print('商品的fn方法')


# 定义手机类
class Phone(Goods):
    def __init__(self, name, price, brand, color):
        # 调用父类的方法，使用关键字super()
        super().__init__(name, price)
        self.color = color
        self.brand = brand

    def fn(self):
        super().fn()
        print('手机的fn方法')

    def __str__(self):
        return self.name


# 调用
phone = Phone('iPhone14', 1800, 'apple', '紫色')
phone.fn()
print(phone.name)
print(phone.price)
print(phone.brand)
print(phone.color)
