"""
一个类，同时继承多个父类
Person类
Pig类
PeiQ类
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('说话')


class Pig:
    def call(self):
        print('🐷叫')


class PeiQ(Person, Pig):
    pass


pq = PeiQ('佩奇', 3)
pq.talk()
pq.call()
