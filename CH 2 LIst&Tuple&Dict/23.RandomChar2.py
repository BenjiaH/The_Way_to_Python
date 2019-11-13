import random

NUM = 10

# 创建空列表
result = []

# 循环十次，生成是个随机数
result = [chr(random.randint(65, 91)) for i in range(10)]
print(result)
