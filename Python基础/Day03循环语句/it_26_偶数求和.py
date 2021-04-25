# 计算0-100的和
result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
        print(i)
    i += 1
    # 每次循环都和result相加
print("0-100之间的偶数求和结果是",result)