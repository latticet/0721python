"""
数据库操作类
类名：DB
    方法：
        read
        write
        init
"""
import pymysql


class DB:
    def __init__(self, database, host='localhost', port=3306, user='root', password='root',
                 cursor_type=pymysql.cursors.Cursor):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                    database=database, charset='utf8')
        self.cursor = self.conn.cursor(cursor_type)
        self.data_result = () if cursor_type == pymysql.cursors.Cursor else []

    def read(self, sql, args=None):
        """读操作"""
        try:
            rows = self.cursor.execute(sql, args)
        except Exception:
            return 0, self.data_result
        else:
            return rows, self.cursor.fetchall()

    def write(self, sql, args=None):
        """写操作"""
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return 0
        else:
            self.conn.commit()
            return rows

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = DB('advanced')
    rows, data = db.read('select * from student')
    # rows, data = db.read('select * from student where stu_id=%s', [100])
    # print(rows)
    # print(data)

    rows = db.write('insert into student(stu_name, stu_no) values("李哈", "stu_no8")')
    if rows:
        print(f'添加成功:{rows}')
    else:
        print(f'添加失败:{rows}')
