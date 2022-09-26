"""
1.实现批量修改目录下的所有文件名(手动创建:file.txt,text.txt,text.py)，
格式为 text_1.txt text_2.py, 在原文件名的基础上,在扩展名前面添加: _数字
"""
import os

# 获取demo目录下的所有资源 - list [file.txt,text.txt,text.py]
file_list = os.listdir('demo')

# 切换到demo目录下
os.chdir('demo')

# 遍历这个列表
i = 1
for file in file_list:
    # 通过file获取名字和后缀
    filename, extension = os.path.splitext(file)  # (filename, extension) -> ('text_1', '.txt')

    # 拼接新的文件名
    # text_1.txt
    new_file = filename + '_' + str(i) + extension
    # 修改文件名
    os.rename(file, new_file)

    i += 1
