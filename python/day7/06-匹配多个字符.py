import re

# *	匹配前一个字符出现0次或者无限次 {0,}
"""
print(re.search('he\w*', 'he'))
print(re.search('he\w*', 'he1'))
print(re.search('he\w*', 'heab'))
print(re.search('he\w*', 'heab_'))
print(re.search('he\w*', 'heab_jfdjas'))
print(re.search('he\w*', 'heab_jfdjas你还'))
print(re.search('he\w*', 'he+ab_jfdjas你还'))
"""

# +	匹配前一个字符出现1次或者无限次 {1,}
"""
print(re.search('he\w+', 'he'))
print(re.search('he\w+', 'he1'))
print(re.search('he\w+', 'heab'))
print(re.search('he\w+', 'he+ab_jfdjas你还'))
print(re.search('he\w+', 'heab_jfdjas你还'))
print(re.search('he\w+', 'hea+b_jfdjas你还'))
"""

# ?	匹配前一个字符出现1次或者0次 {0,1}
"""
print(re.search('he\w?', 'he'))
print(re.search('he\w?', 'he1'))
print(re.search('he\w?', 'heab'))
print(re.search('he\w?', 'he+ab_jfdjas你还'))
"""

# {m}	匹配前一个字符出现m次
"""
print(re.search('he\w{2}', 'he'))
print(re.search('he\w{2}', 'he下'))
print(re.search('he\w{2}', 'he下节课'))
print(re.search('hel{2}', 'he下节课'))
print(re.search('hel{2}', 'hello'))
print(re.search('hel{2}', 'heloo'))
print(re.search('hel{2}', 'helhellao'))
"""

# {m,n}	匹配前一个字符出现从m到n次
"""
print(re.search('he\w{2,5}', 'he'))   # None
print(re.search('he\w{1,4}', 'he下'))
print(re.search('he\w{1,4}', 'he下jkl'))
print(re.search('he\w{1,4}', 'fdskljfdkl he下jklj'))
"""

# {m,}	匹配前一个字符至少出现m次
print(re.search('he\w{2,}', 'he'))   # None
print(re.search('he\w{2,}', 'helei'))
print(re.search('he\w{2,}', 'hele'))
print(re.search('he\w{2,}', 'he12'))
print(re.search('he\w{2,}', 'hexo*'))
print(re.search('he\w{2,}', 'hex*'))
