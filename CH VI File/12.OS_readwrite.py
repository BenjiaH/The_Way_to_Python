# -*- coding: utf-8 -*-

import os

# 以读写、创建的方式打开文件
f = os.open("abc.txt", os.O_RDWR | os.O_CREAT)
# 写入文件内容
len1 = os.write(f, "锄禾日当午，\n".encode("utf-8"))
len2 = os.write(f, "汗滴禾下土。\n".encode("utf-8"))
# 将文件指针移动到开始处
os.lseek(f, 0, os.SEEK_SET)
# 读取文件内容
data = os.read(f, len1 + len2)
# 打印所读取到的字符串
print(data)
# 将字符节恢复成字符串
# data = str(data)
# print(data)
# print(type(data))
# temp = data.replace("'", "")
# print(temp)
# temp = temp.replace("\\x", "")
# print(temp)
# print(temp[1: 37])
# print("0x" + temp[1: 37])
print(data.decode("utf-8"))
os.close(f)
