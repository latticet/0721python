"""
目录操作模块
目录操作模块有以下功能：
创建目录
删除目录（空目录或非空目录）
查找目录中是否存在某个文件

类名：Directory
    方法：
        mkdir
        del_dir
        is_file_in_dir
"""
import os
import shutil


class Directory:
    @staticmethod
    def mkdir(name):
        os.mkdir(name)

    @staticmethod
    def del_dir(name):
        # os.rmdir(name)  # 删除空目录
        shutil.rmtree(name)  # 可以删除非空目录


    def is_file_in_dir(self, dir_name, file_name):
        # 获取目录下的所有资源
        resource = os.listdir(dir_name)
        # return file_name in resource

        # for filename in resource:
        #     if filename == file_name:
        #         return True
        # else:
        #     return False


if __name__ == '__main__':
    # Directory.mkdir('dir1')

    # Directory.del_dir('dir1')

    # print(os.listdir('dir1'))   # ['1.txt', '2.txt']

    # print('3.txt' in ['1.txt', '2.txt'])
    pass







