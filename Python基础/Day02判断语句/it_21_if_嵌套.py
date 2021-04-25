# 定义布尔是否有票
has_ticket = True

# 定义到的长度
knife_length = 30

# 检查是否有票
if has_ticket:
    # 有安检
    # 判断刀的长度
    if knife_length >= 20:
        # 如果大于20
        print("刀长%d ! 收缴!!!"%knife_length)
    else:
        # 允许上车
        print("准您路途愉快")
else:
    # 无买票
    print("请先买票")