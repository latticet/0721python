"""
B类继承A类
B类：子类
A类：父类
"""


class A:
    def __init__(self):
        self.name = '梁金兰'
        self.age = 18


class B(A):
    pass


b = B()
print(b.name)
print(b.age)
