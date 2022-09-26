class Demo:
    @staticmethod  # 语法形式叫做装饰器
    def info():
        print('info')


# 调用
# 类调用静态方法[建议类调用]
Demo.info()
# 对象调用静态方法
Demo().info()
