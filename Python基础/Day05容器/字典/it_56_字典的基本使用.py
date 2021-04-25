xiaoming_dict = {"name":"小明"}
# 1. 取值
print(xiaoming_dict["name"])
# 2. 增加/修改
# 如果key不存在则添加如果存在就修改
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "张三"
print(xiaoming_dict)
# 3. 删除如果存在就就删除不存在就报错
xiaoming_dict.pop("name")
print(xiaoming_dict)

# 统计键值对的数量
print(len(xiaoming_dict))
# 合并字典
temp_dict = {"height":1.75,
             "age":20}
# 注意在合并时包含原有的字典时,会覆盖
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
# 清空字典
xiaoming_dict.clear()
print(xiaoming_dict)