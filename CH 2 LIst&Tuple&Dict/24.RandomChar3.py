import numpy

NUM = 10

# 创建空列表
result = []

# numpy.random.randint()函数可生成一个随机数的矩阵，可生成多行、多列的随机数
# numpy.random.randint(65, 91, [NUM, 1]) 生成一列，NUM行个随机数
result = [chr(i) for i in numpy.random.randint(65, 91, [NUM, 1])]
print(result)
