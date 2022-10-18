import time

from common.base import Base, get_driver
from selenium.webdriver.common.by import By


class LoginPage(Base):
    login_url = 'https://ecshop.test2.shopex123.com/user.php'

    def input_username(self, content):
        self.send_keys((By.NAME, 'username'), content)

    def input_password(self, content):
        self.send_keys((By.NAME, 'password'), content)

    def input_remember(self):
        self.click((By.ID, 'remember'))

    def input_submit(self):
        self.click((By.NAME, 'submit'))


if __name__ == '__main__':
    # 创建driver
    driver = get_driver()
    driver.get('https://ecshop.test2.shopex123.com/user.php')
    # 创建页面对象
    login = LoginPage(driver)
    time.sleep(1)
    login.input_username('fine1')
    time.sleep(1)
    login.input_password('123456')
    time.sleep(1)
    login.input_remember()
    time.sleep(1)
    login.input_submit()

    login.quit(3)
