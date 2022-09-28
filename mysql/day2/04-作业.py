import  pymysql
# 根据学生姓名删除学生信息
name = input('name：')

# conn = pymysql.connect(user='user', password='root', database='advanced')
# cursor = conn.cursor()

sql = 'delete from student where stu_name = ' + '"' + name + '"'
print(sql)
# cursor.execute()

