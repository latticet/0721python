# TODO 1.导入pymysql
import pymysql

# TODO 2.创建连接对象
# host:主机地址（mysql服务的地址），默认：localhost
# user:账号 password：密码
# port：端口号，默认3306
# database: 要操作的数据库
# charset： 通信编码，写utf8
conn = pymysql.connect(host='localhost', user='root', password='root',
                database="advanced", port=3306, charset='utf8')

# TODO 3.获取游标对象
# TODO 指定游标类型
# 元组游标（默认）  pymysql.cursors.Cursor
# 字典游标        pymysql.cursors.DictCursor
# cursor = conn.cursor(cursor=pymysql.cursors.Cursor)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# TODO 4.执行sql语句
# 返回受影响行数
rows = cursor.execute('select * from student')
print(f'受影响行数:{rows}')

# TODO 5.获取结果集
# 每次获取一条记录
# 说明：游标对象的结果集只能获取一次
one = cursor.fetchone()
print(one)
# 指定获取条数：size指定获取的条数
many = cursor.fetchmany(2)
print(many)
# 获取全部
all = cursor.fetchall()
print(all)

# TODO 6.关闭游标对象
cursor.close()

# TODO 7.关闭连接对象
conn.close()
