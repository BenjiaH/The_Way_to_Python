# 要求用户输入一个数 
# 第一行输出十进制
# 第一行输出十六进制
# 第一行输出八进制
# 第一行输出二进制 

num1 = int(input("请输入一个整数："))

# print(type(num1))
print(num1)
print("十六进制:%x" % num1)
print("八进制:%o" % num1)

# 字符串格式化输出不支持二进制输出  C语言好像也是
# print("二进制:%b" % num1) 报错
