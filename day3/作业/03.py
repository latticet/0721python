"""
定义一个高级字符串工具类具有如下方法: 将给定字符串反转（传入abcd返回dcba）
"""


class Tools:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]


tools = Tools('hello')
print(tools.reverse())
