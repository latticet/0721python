import re

# 匹配到返回对象
re_obj1 = re.search('hello', 'jhellofdslakjflkdshellojalkfds')
re_obj2 = re.search('good', 'applegood111goodxxx')
# 匹配到对象的情况下，对象上有一个方法：group(),这个方法返回匹配到的字符串
print(re_obj2.group())

# 匹配不到返回None
re_obj3 = re.search('world', 'applegood111goodxxx')
print(re_obj3)



