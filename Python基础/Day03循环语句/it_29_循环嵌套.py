row = 1
while row <= 5:
    print("*"*row)
    row += 1

print("_"*15)

row2 = 1
while row2 <= 5:
    col2 = 1
    while col2 <= row2:
        print("*",end="")
        col2 += 1
    print("")
    row2 += 1
