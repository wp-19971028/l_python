# 计算0-100的和
result = 0
i = 0
while i <= 100:
    print(i)
    result += i
    i += 1
    # 每次循环都和result相加
print("0-100之间的求和结果是",result)