"""
class NameError(Exception):
    def __str__(self):
        return '异常描述信息'
"""


# TODO 自定义异常类
# 需要继承自Exception
class LenError(Exception):
    def __str__(self):
        return '长度不符合规范'


# TODO 自定义异常抛出
# 语法：raise 异常对象

# TODO 需求：验证用户名长度3-8位，不是就抛出异常。
# 接收用户名
username = input('用户名：')
try:
    if len(username) < 3 or len(username) > 8:
        raise LenError()
    else:
        print('用户名验证通过')
except Exception as e:
    print(e)
