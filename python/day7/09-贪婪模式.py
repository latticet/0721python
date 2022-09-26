import re

# 贪婪模式（默认）
print(re.search('he\w*', 'heab_jfdjas你还'))

# 非贪婪模式 在数量元字符的后面添加一个？
print(re.search('he\w*?', 'heab_jfdjas你还'))
