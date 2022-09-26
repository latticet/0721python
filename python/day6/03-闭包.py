# 闭包
def wrapper(num):

    def inner():
        print(num)
    return inner


# 使用
inner = wrapper(10)
inner()




