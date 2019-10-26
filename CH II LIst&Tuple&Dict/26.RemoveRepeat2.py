import random

# 使用推导式来创建一个包含重复元素的列表
src_list = [random.randint(20, 30) for i in range(15)]
print(src_list)

# 用新列表搜集法：只搜集不重复的元素
target_list = list(set(src_list))	
print(target_list)