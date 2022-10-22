import time

from common.base import Base, By
from common.functions import open_browser
from page.reception.login_page import LoginPage
from common.functions import host


class AddressPage(Base):

    @staticmethod
    def address_locator(index='last()'):
        """
        将整个收货地址当做一个整体,定位
        :param index:
        :return:
        """
        # 省市区
        provinces_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr/td[2]/select[2]')
        cities_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr/td[2]/select[3]')
        districts_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr/td[2]/select[4]')
        # 收货人姓名
        consignee_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[2]/td[2]/input')
        # 邮箱
        email_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[2]/td[4]/input')
        # 详细地址
        address_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[3]/td[2]/input')
        # 邮编
        zipcode_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[3]/td[4]/input')
        # 电话
        telephone_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[4]/td[2]/input')
        # 手机
        mobile_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[4]/td[4]/input')
        # 确认修改
        update_address_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[5]/td[2]/input')
        # 删除
        delete_address_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[5]/td[2]/input[2]')
        # 新增收货地址
        insert_address_loc = ('xpath', f'//form[@name="theForm"][{index}]/table/tbody/tr[5]/td[2]/input')
        if index == 'last()':
            return {'provinces_loc': provinces_loc,  # 省
                    'cities_loc': cities_loc,  # 市
                    'districts_loc': districts_loc,  # 区
                    'consignee_loc': consignee_loc,  # 收货人姓名
                    'email_loc': email_loc,  # 收货人邮箱
                    'address_loc': address_loc,  # 详细地址
                    'zipcode_loc': zipcode_loc,  # 邮编
                    'telephone_loc': telephone_loc,  # 电话号码
                    'mobile_loc': mobile_loc,  # 手机号码
                    'insert_address_loc': insert_address_loc  # 新增收货地址按钮
                    }
        else:
            return {'provinces_loc': provinces_loc,  # 省
                    'cities_loc': cities_loc,  # 市
                    'districts_loc': districts_loc,  # 区
                    'consignee_loc': consignee_loc,  # 收货人姓名
                    'email_loc': email_loc,  # 收货人邮箱
                    'address_loc': address_loc,  # 详细地址
                    'zipcode_loc': zipcode_loc,  # 邮编
                    'telephone_loc': telephone_loc,  # 电话号码
                    'mobile_loc': mobile_loc,  # 手机号码
                    'update_address_loc': update_address_loc,  # 修改收货地址
                    'delete_address_loc': delete_address_loc,  # 删除收货地址
                    }

    def input_consignee(self, name, index='last()'):
        """输入收货人姓名"""
        self.send_keys(self.address_locator(index)['consignee_loc'], name)

    def delete_address(self):
        self.click(self.address_locator("1")['delete_address_loc'])

    def a_user_center(self):
        """进入用户中心"""
        self.click((By.LINK_TEXT, '用户中心'))

    def a_address(self):
        self.click((By.PARTIAL_LINK_TEXT, '收货地址'))


if __name__ == '__main__':
    driver = open_browser()
    login = LoginPage(driver)
    login.get(login.login_url)
    login.member_login()
