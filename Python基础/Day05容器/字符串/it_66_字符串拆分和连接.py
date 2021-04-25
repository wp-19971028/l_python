poem = """\t登鹳雀楼\t王之涣 
        \t\n白日依山尽                          
        \t\n黄河入海流
        \t\n欲穷千原目
        \t\n更上一层楼"""
print(poem)
# 拆分字符串
poemlist = poem.split()
print(poemlist)
# 合并字符串
result = "".join(poemlist)
print(result)