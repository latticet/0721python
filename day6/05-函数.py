"""
1。 函数定义的时候，函数体里面的内容不会执行
2. 只有函数调用的时候，函数体里面的内容才会执行
3. 读一个函数先看这个函数的返回值，在哪儿调用在哪儿返回
"""
# 定义
def fn1():
    for i in range(100):
        print(i)

    print(100)

    def fn2():
        print('fn2')

    def fn3():
        for i in range(1000):
            print(i)

# 调用
result = fn1()
print(result)

