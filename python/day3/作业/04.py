"""
定义一个文件操作类File，方法有：读取所有内容，读取数据按行返回，写入内容，追加数据。
   有以下类方法：
   File.read(文件名)
   File.write(文件名,’内容’)
   File.readlines(文件名)
   File.append(文件名,’内容’)
"""


class File:
    def read(self, filename):
        """读取所有内容"""
        # 打开文件 - r
        f = open(f'resource/{filename}', encoding='utf8')
        # 操作文件
        content = f.read()
        # 关闭文件
        f.close()
        return content

    def write(self, filename, content):
        """写入内容"""
        # 打开文件 - w
        f = open(f'resource/{filename}', mode='w', encoding='utf8')

        # 传参方式
        # 位置传参： 按形参顺序传入实参
        # 关键字传参： 按形参的名字传入实参

        # 操作文件
        f.write(content)
        # 关闭文件
        f.close()
        print('写入成功')

    def read_lines(self, filename):
        """读取数据按行返回"""
        # 打开文件 - r
        f = open(f'resource/{filename}', 'r', encoding='utf8')
        # 文件操作
        content_list = f.readlines()
        # 关闭文件
        f.close()

        return content_list

    def append(self, filename, content):
        """追加数据"""
        # 打开文件 - a
        f = open(f'resource/{filename}', 'a', encoding='utf8')
        # 操作文件
        f.write(content)
        # 关闭文件
        f.close()


file = File()
#
# print(file.read('demo1.txt'))
# file.write('demo2.txt', 'demo2 content')
# print(file.read_lines('demo2.txt'))
# print(file.read_lines('demo1.txt'))

file.append('demo3.txt', 'abc\n')
file.append('demo3.txt', 'def\n')
file.append('demo3.txt', 'ghk\n')
