poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千原目",
        "更上一层楼"]
for poem_str in poem:
    # 居中对齐
    print("|%s|" % poem_str.center(10, "　"))
print("*"*20)
for poem_str in poem:
    # 向左对齐
    print("|%s|" % poem_str.ljust(10, "　"))
print("*"*20)
for poem_str in poem:
    # 向右对齐
    print("|%s|" % poem_str.rjust(10, "　"))
