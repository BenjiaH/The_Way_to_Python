import random
import itertools

# 使用推导式来创建一个包含重复元素的列表
src_list = [random.randint(20, 30) for i in range(15)]
print(src_list)

src_list.sort()

# 进行分组：相同的元素就分成同一组，因此不同的组当然就是不同的元素
it = itertools.groupby(src_list)
# 遍历各组，因此得到都是不同的元素(去重)
for k, g in it:
    print(k, end=", ")
