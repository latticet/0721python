import os
def fn1():
    return 1, 'a', ['hello', 'good'], (100, 200), True


tuple1 = fn1()
print(tuple1)


filename, extension = os.path.splitext('demo.txt')  # (demo, .txt)



def fn2():
    for i in range(10):
        print(i)

    def fn4():
        def fn3():
            print('fn3')
        fn3()

    fn4()


print(fn2())

