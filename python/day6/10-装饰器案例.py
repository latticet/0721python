"""
论坛：
发帖功能
评论功能
"""


def login_decorator(fn):
    def inner(*args, **kwargs):
        print('登录认证')
        return fn()
    return inner


@login_decorator
def post():
    # 登录
    print('发帖')


@login_decorator
def comment():
    # 登录
    print('评论')


@login_decorator
def other():
    # 登录
    print('其他')


if __name__ == '__main__':
    post()
    comment()
    other()