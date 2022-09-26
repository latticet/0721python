"""
注意：
必须在终端下执行这个脚本，才能给程序传参
"""
import sys


# 接收通过python指令执行脚本传入的参数
print(sys.argv)

name = sys.argv[1]
age = sys.argv[2]

print(name)
print(age)


