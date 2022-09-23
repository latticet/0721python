"""
timedelta: 用来计算时间的单位
"""
from datetime import datetime, timedelta

# 准备一个时间对象
datetime_obj = datetime.now()


# 获取7天前的时间
day7 = timedelta(weeks=1)
print(datetime_obj - day7)

# 获取7天后的时间
print(datetime_obj + day7)


