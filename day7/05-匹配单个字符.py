import re
# 正则语句
# 原字符 ：字符本来的含义
# 元字符 ：具有特殊函数以的字符

# .	匹配任意1个字符（除了\n）
"""
print(re.search('he.', 'hea').group())
print(re.search('he.', 'he.').group())
print(re.search('he.', 'he+').group())
re_obj = re.search('he.', 'he0')
print(re_obj.group())
print(re.search('he.', 'he\n'))   # 匹配不到
"""

# [ ]	匹配[ ]中列举任意一个字符
"""
print(re.search('hello[abc]', 'helloa'))
print(re.search('hello[abc]', 'hellob'))
print(re.search('hello[abc]', 'helloc'))
print(re.search('hello[abc]', 'hellod'))   # 匹配不到
# 匹配0-9之间的任意一个数字 [0-9]
print(re.search('he[0-9]', 'he1'))
print(re.search('he[0-9]', 'he7'))
print(re.search('he[0-9]', 'he9'))
print(re.search('he[0-9]', 'hea'))  # 匹配不到
# 匹配26个小写字母 [a-z]
print(re.search('he[a-z]', 'heb'))
print(re.search('he[a-z]', 'heB')) # 匹配不到
# 匹配26个大写字母 [A-Z]
print(re.search('he[A-Z]', 'heT'))
print(re.search('he[A-Z]', 'hef')) # 匹配不到
# 匹配中文汉字
print(re.search('he[\u4e00-\u9fa5]', 'he你好'))
print(re.search('he[\u4e00-\u9fa5]', 'he天气'))
print(re.search('he[\u4e00-\u9fa5]', 'hed'))
"""

# \d	匹配数字，即0-9  [0-9]
"""
print(re.search('he\d', 'he1'))
print(re.search('he\d', 'he7'))
print(re.search('he\d', 'hef'))  # 匹配不到
"""

# \D	匹配非数字，即不是数字
"""
print(re.search('he\D', 'hef'))
print(re.search('he\D', 'he-'))
print(re.search('he\D', 'he*'))
print(re.search('he\D', 'he0'))  # 匹配不到
"""

# \s	匹配空白，即 空格，tab键, \n
"""
print(re.search('he\s', 'he '))
print(re.search('he\s', 'he '))
print(re.search('he\s', 'he\n'))
print(re.search('he\s', 'he\t'))
"""

# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字 等价：[0-9a-zA-Z_\u4e00-\u9fa5]
print(re.search('he\w', 'he1'))
print(re.search('he\w', 'hea'))
print(re.search('he\w', 'he_'))
print(re.search('he\w', 'he你好'))
print(re.search('he[0-9a-zA-Z_\u4e00-\u9fa5]', 'he你好'))
print(re.search('he\w', 'he-'))  # 匹配不到
print(re.search('he\w', 'he+'))  # 匹配不到
print(re.search('he\w', 'he*'))  # 匹配不到
print(re.search('he\w', 'he&'))  # 匹配不到

# \W 匹配特殊字符，即非字母、非数字、非汉字、非下划线