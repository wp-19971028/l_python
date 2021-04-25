hello_str = "hello world"
# 判断是不是以指定字符串开始
print(hello_str.startswith("hello"))
# 判断是不是以指定字符串结束
print(hello_str.endswith("world"))
# 判断是不是含有指定字符串
print(hello_str.find("llo"))
# index查不到会报错
print(hello_str.index("llo"))
# 替换字符串
print(hello_str.replace("world", "python"))  # hello python
print(hello_str)  # hello world
