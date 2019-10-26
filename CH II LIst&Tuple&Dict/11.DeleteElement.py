my_list = ["python", "swift", "lua", "kotlin", "js"]

del my_list[2]# 删除第三个元素
print(my_list)

my_list.extend(range(30, 35))
print(my_list)

del my_list[4: 7]
print(my_list)