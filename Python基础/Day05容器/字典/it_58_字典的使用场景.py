# 使用多个键值对对一个物体的相关信息存储 ---数据类型很复杂
# 将字典放在一个列表中进行操作
card_list = [
    {"name": "张三",
     "qq": "123456",
     "phone": "654123"},

    {"name": "李四",
     "qq": "654321",
     "phone": "110"},

    {"name": "王五",
     "qq": "987456",
     "phone": "110"}
]
for card_info in card_list:
    print(card_info)
