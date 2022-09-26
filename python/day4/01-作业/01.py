"""
1. 定义一个模块(新建一个python文件)
模块里面具有 三个类
厨师: 炒菜方法
服务员: 接待客人方法 送走客人方法
收银员: 收钱方法
客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收营员收钱-->服务员送客
"""


class Cooker:
    @staticmethod
    def cook():
        print('炒菜')


class Waiter:
    @staticmethod
    def reception():
        print('接待')

    @staticmethod
    def send():
        print('送走客人')


class Cashier:
    @staticmethod
    def money():
        print('收钱')


# 客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收营员收钱-->服务员送客
print('客人来')
Waiter.reception()
print('客人点菜')
Cooker.cook()
print('客人吃完了')
Cashier.money()
Waiter.send()
