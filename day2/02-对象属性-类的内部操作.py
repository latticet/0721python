"""
类的内部：
对象属性操作，就是在对象方法里面，通过self来操作属性
"""


class Person:
    def set_name(self):
        # 设置属性
        self.name = '祝子芸'

    def get_name(self):
        # 获取属性
        print(self.name)

    def edit_name(self):
        # 修改属性
        self.name = '钟永佳'

    def del_name(self):
        # 删除属性
        del self.name


p1 = Person()
p1.set_name()
p1.get_name()
p1.edit_name()
print(p1.name)
p1.del_name()

print(p1.name)
