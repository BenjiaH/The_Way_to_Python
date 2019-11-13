# 创建列表用list函数
my_list = list(range(2, 10))

# 创建元组用tuple函数
my_tuple = tuple(range(4, 8))

# my_tuple(0) = my_list[3]
print(my_list)
print(my_tuple)

# 将元组转为列表
list2 = list(my_tuple)
print(list2)

# 将列表转成元组
tuple2 = tuple(my_list)
print(tuple2)
