import random

NUM = 10

# 创建空列表
result = []

# 循环十次，生成是个随机数
for i in range(10):
	# 生成不包括 65-91 的随机数
	n = random.randint(65, 91)
	result.append(chr(n))

print(result)