"""
第一级别： python内置  built-in
第二级别:  sys.path = [
脚本当前所在的目录,
系统标准包模块
第三方包模块   requests.py
]
"""

import time

# TODO time.sleep(n)  设置程序的休眠时间，n传入正整数
"""
time.sleep(2)
print(111111)
"""

# TODO time.time()	返回一个距Epoch的秒数，是浮点数。从1970年1月1日0时0分0秒到现在的秒数
"""
while True:
    print(time.time())
"""

# time.gmtime(seconds)	将秒数转化为年月日时分秒，以UTC时间为标准。
"""
print(time.gmtime())
print(time.gmtime(120))
"""

# time.localtime(seconds)	将秒数转化为年月日时分秒，以当地时间为标准。
"""
print(time.localtime())
print(time.localtime(120))
"""

# time.ctime(seconds)	返回年月日时分秒的字符串。
"""
print(time.ctime())
print(type(time.ctime()))
"""

# time.asctime(tuple)	从struct_time返回年月日时分秒字符串。
"""
struct_time = time.localtime(120)
print(time.asctime(struct_time))
"""

# time.mktime(tuple)	将struct_time转换为秒数。
"""
struct_time = time.localtime(120)
print(time.mktime(struct_time))
"""

# time.strftime(fmt,t)	按照fmt格式将struct_time显示成字符串。
"""
struct_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))
"""

# time.strptime(str,fmt)	将年月日时分秒的字符串按照fmt解析成struct_time结构。
str_time = "2022-09-23 10:20:09"
struct_time = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print(struct_time)


