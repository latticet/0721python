# 形参
def fn1(a, b, c=10, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)


# 实参
# 位置传参
fn1(1, 2, 3, 4, 'hello', 'good')

# 关键字传参
fn1(a=100, c=1000, b=10000, d=200)


def open(filename, mode, xx, enconding):
    pass


open('a.txt', 'r', 'utf8')
