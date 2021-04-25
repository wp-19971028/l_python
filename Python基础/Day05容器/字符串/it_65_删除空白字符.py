poem = ["\t\n登鹳雀楼",
        "\t\n王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千原目",
        "更上一层楼"]
for poem_str in poem:
    # 居中对齐
    print("|%s|" % poem_str.strip().center(10, "　"))