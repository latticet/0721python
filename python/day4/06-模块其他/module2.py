name = 'module2'


def fn2():
    print('fn2执行了')


# print('==' * 20)
# 模块方式执行： 模块名
# 脚本方式执行： __main__
# print(__name__)

# 如果__name__值是__main__， 当前文件就是以脚本方式执行
if __name__ == '__main__':
    fn2()
