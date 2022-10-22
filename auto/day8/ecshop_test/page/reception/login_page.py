import time
from common.base import Base, By
from common.functions import open_browser, host


class LoginPage(Base):
    login_url = host + 'user.php'

    def input_username(self, content):
        self.send_keys((By.NAME, 'username'), content)

    def input_password(self, content):
        self.send_keys((By.NAME, 'password'), content)

    def input_remember(self):
        self.click((By.ID, 'remember'))

    def input_submit(self):
        self.click((By.NAME, 'submit'))

    def member_login(self):
        self.input_username('fine1')
        self.input_password('123456')
        self.input_submit()


if __name__ == '__main__':
    # 创建driver
    driver = open_browser()
    # 创建页面对象
    login = LoginPage(driver)
    login.get(login.login_url)
    time.sleep(1)
    login.input_username('fine1')
    time.sleep(1)
    login.input_password('123456')
    time.sleep(1)
    login.input_remember()
    time.sleep(1)
    login.input_submit()

    login.quit(3)
