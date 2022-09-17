"""
单例模式实现
"""


class Singleton:
    # 类属性
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


p1 = Singleton()
p2 = Singleton()
p3 = Singleton()
p4 = Singleton()

print(p1)
print(p2)
print(p3)
print(p4)
