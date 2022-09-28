"""
一次性添加5条记录
"""
# 1。导入pymysql
import pymysql
from datetime import datetime

# 2。创建连接对象
conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')

# 3. 创建游标对象
cursor = conn.cursor()

try:
    # 4. 执行sql语句
    # 5. 提交或者回滚
    for i in range(1, 6):
        sql = f"INSERT INTO news VALUES(NULL, 'title{i}', 'author{i}', 'content{i}', '{datetime.now()}', {i})"
        print(sql)
        rows = cursor.execute(sql)
        print(rows)
except Exception as e:
    print(e)
    conn.rollback()
else:
    conn.commit()

# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
