"""
1. 定义一个包（就是目录）
文件操作模块
文件操作模块有以下功能(写在类里面的函数)：
读取文件内容
写入内容到文件中
复制文件
删除文件
文件改名

类名 File：
    方法：
        read
        write
        copy
        delete
        rename
"""
import os

class File:
    def read(self, file):
        f = open(file, encoding='utf8')
        content = f.read()
        f.close()
        return content


    def write(self, file, content):
        f = open(file, 'w', encoding='utf8')
        f.write(content)
        f.close()

    def copy(self, file):  # demo.txt
        # 准备新文件名称
        old_filename, extension = os.path.splitext(file)  # ('demo', '.txt')
        # 拼接新文件名
        new_filename = old_filename + '-副本' + extension

        # 复制操作
        # 打开源文件
        old_file = open(file, 'rb')
        # 打开新文件
        new_file = open(new_filename, 'wb')

        while True:
            # 读取源文件的内容
            content = old_file.read(1024)
            if not content:
                break
            # 写入新文件中
            new_file.write(content)

        # 关闭资源
        old_file.close()
        new_file.close()

    @staticmethod
    def delete(file):
        os.remove(file)

    @staticmethod
    def rename(file, new_file):
        old_filename, extension = os.path.splitext(file)  # ('demo', '.txt')
        new_filename = new_file + extension
        os.rename(file, new_filename)


if __name__ == '__main__':
    # print(File().copy('demo.txt'))
    # 复制操作
    # File().copy('test01.md')
    # File().copy('午唱.docx')
    # File().copy('01-项目进度.mp4')

    # 删除文件
    # File.delete('test01-副本.md')
    # 修改文件名
    # File.rename('test01.md', 'mytest01')
    pass



