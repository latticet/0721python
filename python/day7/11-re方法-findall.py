import re

# findall方法
"""
str1 = 'fjdhellosfhellojlkhellodskl'
print(re.findall('hello', str1))  # list
"""

# flags参数
# re.I
"""
print(re.search('He\w{3}', 'Hello'))
print(re.search('He\w{3}', 'hello'))
print(re.search('He\w{3}', 'hello', re.I))   # Ignore(忽略)
"""

# re.S  Space
print(re.search('he.', 'hex'))
print(re.search('he.', 'he+'))
print(re.search('he.', 'he-'))
print(re.search('he.', 'he\n'))
print(re.search('he.', 'he\n', re.S))


