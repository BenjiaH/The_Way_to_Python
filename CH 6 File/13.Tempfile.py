# -*- coding: utf-8 -*-

import tempfile

# 创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)
fp.write("床前明月光，".encode("utf-8"))
fp.write("疑是地上霜。".encode("utf-8"))
# 将文件指针移到开始处，准备读取文件
fp.seek(0)
print(fp.read().decode("utf-8"))  # 输出刚才写入的内容
# 关闭文件，文件自动删除
fp.close()

# 通过with语句创建临时文件，with会自动关闭临时文件
with tempfile.TemporaryFile() as fp:
    # 写入内容
    fp.write(b"I Love Python")
    # 将文件指针移到开始处，准备读取文件
    fp.seek(0)
    # 读取文件内容
    print(fp.read())

# 通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print("创建临时目录", tmpdirname)
