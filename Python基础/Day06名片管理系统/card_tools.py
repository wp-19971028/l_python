card_list = []


def show_menu():
    """
    显示菜单
    :return: null
    """
    print("*" * 50)
    print("欢迎使用[名片管理系统]")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:
    """
    print("-" * 50)
    print("新增名片")
    # 1. 提示用户输入名片详细信息
    # shift + f6 重命名变量
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话号码:")
    qq_str = input("请输入QQ号码")
    email_str = input("请输入邮箱:")
    # 2. 使用用户输入信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典添加到列表
    card_list.append(card_dict)
    print(card_list)
    # 4. 提示用户添加成功
    print("添加 %s 的名片成功成功!" % name_str)


def show_all():
    """
    显示所有名片
    :return:
    """
    print("-" * 50)
    print("显示名片内容")
    # 判断是否存在名片记录如不存在就返还
    if len(card_list) == 0:
        print("当前没有名片记录,请使用新增名片添加记录")
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("=" * 50)
    # 遍历列表依次输出字典信息

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"],
                                            ))


def search_card():
    """
    搜索名片
    :return:
    """
    print("搜索名片")
    # 1. 提示用户要输搜索的姓名
    find_name = input("请输入姓名搜索:")

    # 2. 遍历列表查找要搜索的性姓名,如果没找到,提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了")
            # 打印表头
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")

            print("=" * 50)
            # 遍历列表依次输出字典信息
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"],
                                                ))
            # TODO 针对找到的名片操作
            deal_card(card_dict)
            break
        else:
            print("抱歉没有找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请输入要执行的操作"
                       "[1] 修改 [2]删除 [3]返回上一级"
                       ":")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱")
        print("修改名片")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")
    else:
        pass


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value:  字典原有的值
    :param tip_message: 提示信息
    :return: 如果输入为空返回原有值如果不为空则返回输入信息
    """
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户输入进行判断,如果输入内容则直接返还
    if len(result_str) > 0:
        return result_str
    # 如果输入内容为空 则返回原有的值
    else:
        return dict_value
