# datetime模块下面的datetime类
import time
from datetime import datetime

# datetime的类方法
# datetime.today()	当前时间，localtime。
"""
datetime_obj = datetime.today()
print(datetime_obj)
print(type(datetime_obj))
"""

# datetime.now()	当前的时间。
"""
datetime_obj = datetime.now()
print(datetime_obj)
"""

# datetime.utcnow()	当前格林时间。
"""
datetime_obj = datetime.utcnow()
print(datetime_obj)
"""

# datetime.fromtimestamp()	将时间戳的转换为时间。
"""
times = time.time()
datetime_obj = datetime.fromtimestamp(times)
print(datetime_obj)
"""

# TODO datetime.strptime(str,fmt)	按照fmt的格式解析字符串生成datetime。
"""
datetime_str = "2022-10-1 10:10:10"
datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
print(datetime_obj)
print(type(datetime_obj))
"""

# datetime的对象方法
datetime_obj = datetime.now()
# datetime.date()	返回一个date对象。
"""
date_obj = datetime_obj.date()
print(date_obj)
print(type(date_obj))
"""

# datetime.time()	返回time对象。
"""
time_obj = datetime_obj.time()
print(time_obj)
print(type(time_obj))
"""

# TODO datetime.strftime(fmt)	按照fmt的格式将datetime对象转化为字符串。
print(datetime_obj.strftime('%Y%m%d %H%M%S'))
print(datetime_obj.strftime('%Y/%m/%d %H:%M:%S'))


