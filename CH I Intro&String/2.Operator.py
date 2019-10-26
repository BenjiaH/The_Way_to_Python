import math

print(3 ** 3)
print(36 ** 0.5)
print(27 ** (1 / 3))

print(math.sin((math.pi) / 4))
print(math.pi)

# 索引操作符
s = "fkjava.org"
print(s[3])
print(s[3: 7])
print(s[3: 7: 2])
# 索引运算符，对所有序列（字符串、字节串、列表、元组）都支持

s1 = "213"
s2 = str(213)
# s1 s2引用的不是同一个字符串
print(s1 is s2)# is 判断两个变量引用是否相等
print(s1 == s2)# == 只判断他们的值是否相等

age = int(input("请输入年龄："))
if age > 25:
	print("年龄大于25.")
# 在Python中以缩进判断是否为同一语句
print("111")
	
if age <= 25:
	print("年龄小于25.")