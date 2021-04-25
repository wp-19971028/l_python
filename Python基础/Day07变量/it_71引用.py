def test(num):
    print("%d变对应的内存地址是%d"% (num,id(num)))

# 定义一个数字变量
a = 10
# 数据地址本质是一个数字
print("a变量的内存地址是%d"%id(a))

# 调用test函数
test(a)

# 定义一个字符串变量
result = "hello"
print("函数的内存是%d"%id(result))