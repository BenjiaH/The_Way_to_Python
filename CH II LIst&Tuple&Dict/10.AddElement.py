my_list = ["python", "swift"]
# 增加一个元素
my_list.append("kotlin")
print(my_list)

# 为列表 append列表，列表将被当成整体
my_list.append(list(range(3, 6)))
print(my_list)

# extend用于将序列中的元素添加进来
my_list.extend(range(20, 25))
print(my_list)


my_list.extend("fkjava") # 字符串本身就是序列
print(my_list)

# 将lua插入到第四个元素
my_list.insert(3, "lua")
print(my_list)

