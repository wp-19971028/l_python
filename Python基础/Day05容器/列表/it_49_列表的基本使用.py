name_list = ["张三","李四","王五"]
# 获取索引值
print(name_list[0])
# 获取元素位置
print(name_list.index("李四"))
# 修改
print(name_list)
name_list[1] = "李斯"
print(name_list)
# 增加
## 追加
name_list.append("王小二")
print(name_list)
## 插入
name_list.insert(1,"李云龙")
print(name_list)
## 扩展
name_list.extend(["孙权","刘备","曹操"])
print(name_list)
# 删除指定数据
name_list.remove("张三")
print(name_list)
# pop默认弹出最后一个元素
name_list.pop()
print(name_list)
# 弹出指定索引
name_list.pop(1)
print(name_list)
# 清空列表
name_list2 = name_list
name_list2.clear()
print(name_list2)

# del删除从内存删除
#del name_list[1]
print(name_list)
name_list3 = ["张三","李四","王五","张三"]
# 统计列表长度
list_len = len(name_list3)
print(list_len)
# 统计列表的中元素出现的次数
print(name_list3.count("张三"))
num = [1,5,3,4,2]
# 升序排序
print(num)
num.sort()
print(num)
# 降序排序
num.sort(reverse=True)
print(num)
# 逆序
num.reverse()
print(num)

