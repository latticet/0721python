# 手机号登录
# 匹配手机号的正则  131 46562211
import re

pattern = '^1[3-9][0-9]{9}$'

phone = input('手机号：')
if re.search(pattern, phone):
    print('手机号合法')
else:
    print('手机号不合法')



