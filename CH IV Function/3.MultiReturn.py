import random

# 返回三个随机的大写字符
def test():
	c1 = chr(random.randint(65, 90))
	c2 = chr(random.randint(65, 90))
	c3 = chr(random.randint(65, 90))
	
	return (c1, c2, c3)
	
	
print(test())