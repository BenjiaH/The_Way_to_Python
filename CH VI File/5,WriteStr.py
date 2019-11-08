# -*-coding:utf-8-*-
import os

f = open("x.txt", "ab+")
# os.linesep代表当前系统上的换位符
f.write(("I love Python" + os.linesep).encode("utf-8"))
f.writelines((("床前明月光，" + os.linesep).encode("utf-8"),
              ("疑是地上霜。" + os.linesep).encode("utf-8"),
              ("举头望明月，" + os.linesep).encode("utf-8"),
              ("低头思故乡。" + os.linesep).encode("utf-8")))
f.close()
