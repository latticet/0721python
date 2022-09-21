"""
类名：Card
    属性：cards = []
    方法：
        add_card()
        show_card()
        update_card()
        del_card()
        run()
"""


class Card:
    def __init__(self):
        # 初始化名片数据
        self.cards = []

    def add_card(self):
        """
        添加名片
        :return:
        """
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
        self.cards.append(new_card)
        # 添加成功,给出友好提示
        print(f"名片[{name}]添加成功.")

    def show_card(self):
        """显示名片"""
        print("==========显示名片==========")
        # 显示标题
        print("姓名\t\t电话\t\t职位\t\t公司名称\t\t地址")

        # 遍历名片盒子(列表)
        for card in self.cards:
            # 从名片盒子cards中遍历出来的名片card是一个字典
            print(f"{card['name']}\t\t{card['tel']}\t\t{card['job']}\t\t{card['company']}\t\t{card['addr']}")

        print("名片显示完成.")

    def update_card(self):
        """修改名片"""
        print("==========修改名片==========")
        # 提示用户输入要修改的名片 姓名
        find_name = input("输入要修改的名片的姓名: ")

        # 遍历名片盒子,查看是否存在该名片
        for card in self.cards:
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
                index = self.cards.index(card)

                # 根据索引修改列表中的数据
                self.cards[index] = new_card
                # 修改完成后给出友好提示
                print(f"名片[{find_name}]修改成功.")

                break  # 已找到名片并修改,退出循环

        else:
            print(f"未找到名片[{find_name}]")

    def del_card(self):
        """删除名片"""
        print("==========删除名片==========")
        # del 列表[索引]
        # 列表.remove(数据)
        # 列表.pop(索引)

        # 提示用户输入要删除的名片的姓名
        find_name = input("输入要删除的名片姓名: ")
        # 遍历名片盒子拿到每张名片(字典)
        for card in self.cards:
            # print(card)
            # 判断名片盒子中是否存在用户要删除的名片
            if card['name'] == find_name:
                # 列表.remove(数据)
                self.cards.remove(card)
                # 删除成功,给出友好提示
                print(f"名片[{find_name}]删除成功.")
                break
        else:
            # 未找到要删除的名片,给出友好提示
            print(f"名片[{find_name}]不存在.")

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
    cards = Card()
    cards.run()