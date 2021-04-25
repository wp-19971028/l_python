import card_tools
while True:
    # TODO(王平) 显示功能菜单
    card_tools.show_menu()
    action_str = input("请选择希望执行的操作:")
    print("您选择的操作是[%s]"% action_str)
    # 1,2,3针对名片的操作
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            card_tools.new_card()
            pass
        # 显示名片
        elif action_str == "2":
            card_tools.show_all()
            pass
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()
            pass
        pass # pass是个站位符不进行任何操作
    # 0 退出系统
    elif action_str == "0":
        # pass
        print("欢饮再次使用,名片管理系统")
        break
    # 其它内容提示错误,重新操作
    else:
        print("您输入的不正确请重新操作")