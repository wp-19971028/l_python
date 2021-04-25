num_str = "1"
num_str2 = "\u00b2"
num_str3 = "三"
# 这三个方法都不可以判断小数
#只可以判断阿拉伯数字
print(num_str.isdecimal())
# 可以判断特殊的数字
print(num_str2)
print(num_str.isdigit())
print(num_str2.isdigit())
# 可以判断汉语数字
print(num_str.isnumeric())
print(num_str2.isnumeric())
print(num_str3.isnumeric())