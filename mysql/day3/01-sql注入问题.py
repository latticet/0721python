"""
需求： 通过学生姓名查询学生信息
"""
# 1。导入pymysql
import pymysql

# 2。创建连接对象
conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')

# 3. 创建游标对象
cursor = conn.cursor()

# 4. 执行sql语句
# 获取学生姓名
name = input('姓名：')
# TODO sql注入问题
# 通过学生姓名查询学生信息
sql = f'select * from student where stu_name = "{name}"' # " or 1 = 1 or "
# 'select * from student where stu_name = "" or 1 = 1 or ""'
rows = cursor.execute(sql)

# 5. 获取结果集
if rows:
    student_tuple = cursor.fetchall()  # ((id, name, no, class, age),())
    for student in student_tuple:
        info_str = ''
        for info in student:
            info_str += str(info) + ','
        print(info_str.rstrip(','))
else:
    print('学生不存在')

# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
