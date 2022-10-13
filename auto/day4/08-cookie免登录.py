from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 设置cookie
cookies = [
    {
        'name': 'BDUSS',
        'value': 'Dh4cjFjWDhDaS1uT3l3NXdwTEhDVzVNeXk0S1diVlhFUEc5STF6c1ZXdnhRMjlqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPG2R2PxtkdjR'
    },
    {
        'name': 'BDUSS_BFESS',
        'value': 'Dh4cjFjWDhDaS1uT3l3NXdwTEhDVzVNeXk0S1diVlhFUEc5STF6c1ZXdnhRMjlqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPG2R2PxtkdjR'
    }
]

for cookie in cookies:
    driver.add_cookie(cookie)

# 刷新页面
driver.refresh()

# driver.quit()
