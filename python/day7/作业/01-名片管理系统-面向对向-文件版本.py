"""
名片管理系统-面向对象-文件版本
"""


class CardsSystem():

    def add_card(self):
        # TODO 从文件中读取名片内容
        cards = self.read_cards()
        print("==========添加名片==========")
        # 提示用户输入要添加的名片信息
        name = input("姓名:")
        tel = input("电话:")
        job = input("职位:")
        company = input("公司名称:")
        addr = input("公司地址:")
        # 将用户输入的名片信息组装成一张新名片[字典]
        new_card = {"name": name, "tel": tel, "job": job, "company": company, "addr": addr}

        # 将新的名片new_card追加到名片盒子[列表]中: 列表.append(数据)
        cards.append(new_card)
        # 添加成功,给出友好提示
        print(f"名片[{name}]添加成功.")

        # TODO 将cards写入文件
        self.write_cards(cards)

    # 定义显示名片函数
    def show_card(self):
        # TODO 从文件中读取名片内容
        cards = self.read_cards()
        print("==========显示名片==========")
        # 显示标题
        print("姓名\t\t电话\t\t职位\t\t公司名称\t\t地址")

        # 遍历名片盒子(列表)
        for card in cards:
            # 从名片盒子cards中遍历出来的名片card是一个字典
            print(f"{card['name']}\t\t{card['tel']}\t\t{card['job']}\t\t{card['company']}\t\t{card['addr']}")

        print("名片显示完成.")

    # 定义修改名片函数
    def update_card(self):
        # TODO 从文件中读取名片内容
        cards = self.read_cards()
        print("==========修改名片==========")
        # 提示用户输入要修改的名片 姓名
        find_name = input("输入要修改的名片的姓名: ")

        # 遍历名片盒子,查看是否存在该名片
        for card in cards:
            # print(card)	# card表示一张名片,字典
            # 判断当前遍历出来的名片姓名与用户输入的姓名是否一致
            if card['name'] == find_name:
                # 提示用户输入新的名片信息
                print("请在下方输入新的名片信息")
                name = input("姓名:")
                tel = input("电话:")
                job = input("职位:")
                company = input("公司名称:")
                addr = input("公司地址:")
                # 将用户输入的名片信息组装成一张新名片[字典]
                new_card = {"name": name, "tel": tel, "job": job, "company": company, "addr": addr}
                # 修改列表中的数据:  列表[索引] = 新值
                # 获取要修改的名片的索引
                index = cards.index(card)

                # 根据索引修改列表中的数据
                cards[index] = new_card
                # 修改完成后给出友好提示
                print(f"名片[{find_name}]修改成功.")

                break  # 已找到名片并修改,退出循环

        else:
            print(f"未找到名片[{find_name}]")

        # TODO 将cards写入文件
        self.write_cards(cards)

    # 定义删除名片函数
    def del_card(self):
        # TODO 从文件中读取名片内容
        cards = self.read_cards()

        print("==========删除名片==========")
        # del 列表[索引]
        # 列表.remove(数据)
        # 列表.pop(索引)

        # 提示用户输入要删除的名片的姓名
        find_name = input("输入要删除的名片姓名: ")
        # 遍历名片盒子拿到每张名片(字典)
        for card in cards:
            # print(card)
            # 判断名片盒子中是否存在用户要删除的名片
            if card['name'] == find_name:
                # 列表.remove(数据)
                cards.remove(card)
                # 删除成功,给出友好提示
                print(f"名片[{find_name}]删除成功.")
                break
        else:
            # 未找到要删除的名片,给出友好提示
            print(f"名片[{find_name}]不存在.")

        # TODO 将cards写入文件
        self.write_cards(cards)

    def read_cards(self):
        """
        读取cards.txt文件中的所有内容，转化为列表字典格式，然后返回
        :return: [{},{},{}, ...]
        """
        # 从文件中以行的形式读取所有内容
        f = open('cards.txt', 'r', encoding='utf8')
        cards_list = f.readlines()
        f.close()

        # 遍历所有行，将字符串转化为列表字典形式
        result = []  # 准备返回的结果
        for card_str in cards_list:
            # 将字符串先取出掉最右侧的\n,然后再用逗号分割列表
            card_list = card_str.rstrip('\n').split(',')
            # 将列表拼接为名片格式的字典
            card_dict = {"name": card_list[0], "tel": card_list[1], "job": card_list[2], "company": card_list[3],
                         "addr": card_list[4]}
            # 将字典追加到结果列表中
            result.append(card_dict)

        return result

    def write_cards(self, cards_list):
        """
        将列表字典类型的数据转化为字符串写入到文件中
        :param cards_list: 列表字典数据
        :return:
        """
        # 打开文件
        f = open('cards.txt', 'w', encoding='utf8')
        # 操作文件
        for card_dict in cards_list:
            # 将字典中的所有value转化为类列表，然后字符串join拼接为字符串
            card_str = ','.join(card_dict.values()) + '\n'
            f.write(card_str)

        # 关闭文件
        f.close()

    def run(self):
        while True:
            # 显示主菜单
            print("\n========欢迎登录源码时代名片管理系统v1.0========\n")
            num = input("功能列表:	[1.添加名片 2.显示名片 3.修改名片 4.删除名片 0.退出系统]")

            # 根据用户的选择执行相应的功能
            if num == "1":
                # 调用添加名片的函数
                self.add_card()

            elif num == "2":
                # 调用显示名片的函数
                self.show_card()

            elif num == "3":
                # 调用修改名片的函数
                self.update_card()

            elif num == "4":
                # 调用删除名片的函数
                self.del_card()

            elif num == "0":
                exit("退出系统")

            else:
                print("输入有误,请输入[0~4]的选项.")


if __name__ == '__main__':
    cards_system = CardsSystem()
    cards_system.run()