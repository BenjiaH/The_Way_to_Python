# 要求用户输入一个数 
# 第一行输出十进制
# 第一行输出十六进制
# 第一行输出八进制
# 第一行输出二进制 

num1 = int(input("请输入一个整数："))

# print(type(num1))
print(num1)
print("十六进制", hex(num1))
print("八进制", oct(num1))
print("二进制", bin(num1))
