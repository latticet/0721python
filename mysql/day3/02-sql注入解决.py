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
# 通过学生姓名查询学生信息
# TODO sql注入解决: 用户输入数据的地方用%s占位符占位
# 注意：sql注入的%s和字符串格式化的%s没有关系
sql = 'select * from student where stu_name = %s'
rows = cursor.execute(sql, [name])

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
