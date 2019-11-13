# -*-coding:utf-8-*-

# f = open("E:\\Users\\Administrator\Desktop\\23test.txt", "rb", True, "utf-8")
f = open("1.File.py", "rb", True)
# 判断文件指针的位置
print(f.tell())
# 将文件指针移动到第三处
f.seek(3)
print(f.tell())
# 读取一个字节文件指针自动后移一个数据
print(f.read(1))
print(f.tell())
# 将文件指针移动到第五处
f.seek(5)
print(f.tell())
# 将文件指针向后移动五
f.seek(5, 1)
print(f.tell())  # 5+5
# 将文件指针移动d到倒数第十
f.seek(-10, 2)
print(f.tell())
print(f.read(1))
