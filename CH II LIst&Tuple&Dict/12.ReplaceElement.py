my_list = ["python", "swift", "lua", "kotlin", "js"]

my_list[-2] = "java"
print(my_list) 

# 被替换部分只有2个元素，替换成4个元素，实际是増加了元素
my_list[2: 4] = ["lua", "java", "go", "erlang"]
print(my_list)

# 被替换部分只有3个元素，替换成1个元素，实际是删除了元素
my_list[2: 5] = ["objecti-c"]
print(my_list)