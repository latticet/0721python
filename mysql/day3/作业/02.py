"""
根据用户输入的标题删除记录（文件二）
"""
# 1。导入pymysql
import pymysql

# 2。创建连接对象
conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')

# 3. 创建游标对象
cursor = conn.cursor()

title = input('标题：')

# 通过标题查询数据是否存在
query_sql = f'select * from news where title = "{title}"'
rows = cursor.execute(query_sql)
if rows:
    # 如果存在进行删除
    try:
        sql = f'delete from news where title = "{title}"'
        rows = cursor.execute(sql)
    except Exception:
        print('删除失败')
        conn.rollback()
    else:
        if rows:
            print('删除成功')
        else:
            print('删除失败')
        conn.commit()
else:
    print('标题不存在')

# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
