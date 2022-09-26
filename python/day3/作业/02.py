"""
新建一个文件，定义一个计算类,有两个属性,数字1,数字2,具有 加 减 乘 除 方法
类名：Calc
    属性：num1, num2
    方法：add subtraction multiplication division
"""


class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """加法"""
        return self.num1 + self.num2

    def subtraction(self):
        """减法"""
        return self.num1 - self.num2

    def multiplication(self):
        """乘法"""
        return self.num1 * self.num2

    def division(self):
        """除法"""
        return self.num1 // self.num2


calc = Calc(4, 2)
print(calc.add())
print(calc.subtraction())
print(calc.multiplication())
print(calc.division())