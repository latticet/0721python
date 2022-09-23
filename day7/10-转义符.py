# 需求：匹配文件名   xxx.txt xxx.mp4 xxx.jpg  xxx.JPG xxx.JPEG xxx.JPG xxx.mp3
import re

# 匹配文件名
# 接收用户输入文件名
"""
while True:
    filename = input('文件名：')

    if re.search('^\w{1,32}\.[a-zA-Z]{1,4}[34]?$', filename):
        print('ok')
    else:
        print('fail')

"""

# hello\doc

pattern = r'\w{1,32}\\\w{1,32}'
print(re.search(pattern, 'hello\doc'))



