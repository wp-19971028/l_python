import random

# 从控制台输入要出的拳头  石头(1) /剪刀 (2)/布(3)
player = int(input("请输入您要出的拳头 石头(1) /剪刀 (2)/布(3):"))
# 电脑随机出圈
computer = random.randint(1,3)
print("玩家出的拳头是%d 电脑出的是%d"%(player,computer))
# 比较胜负
if player in [1,2,3]:
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):

        print("玩家胜利!")
    elif player == computer:
        print("平局!")
    else:
        print("电脑赢了")
else:
    print("请按照准确的规则出拳")
