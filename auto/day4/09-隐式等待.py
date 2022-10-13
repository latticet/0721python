# 163邮箱发送邮件
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://mail.163.com')
driver.implicitly_wait(10)

# TODO 登录操作
# 切换到登录的这个frame
frame_element = driver.find_element(By.XPATH, '//iframe[contains(@id, "x-URS-iframe")]')
driver.switch_to.frame(frame_element)

# 定位账号输入框，输入账号
time.sleep(2)
driver.find_element(By.NAME, 'email').send_keys('itsourcetest')
# 定位密码输入框，输入密码
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('Itsource123.')
# 定位登录按钮，  点击登录
driver.find_element(By.ID, 'dologin').click()
time.sleep(5)
driver.find_element(By.ID, 'dologin').click()

# TODO 点击写信按钮
# 点击信息按钮，进入写信页面
locator = (By.ID, '_mail_component_149_149')
send_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator), message='Fail')
send_element.click()
