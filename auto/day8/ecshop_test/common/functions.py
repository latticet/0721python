from selenium import webdriver

host = 'http://172.16.2.208:8080/ecshop/'


def open_browser(browser='chrome'):
    """
    打开浏览器，返回driver
    :param browser: str
    :return: object
    """
    # 打开浏览器, 设置driver
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'edge':
        return webdriver.Edge()
    else:
        print('不支持该浏览器')
