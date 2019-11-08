# -*-coding:utf-8-*-

f = open("E:\\Users\\Administrator\Desktop\\23test.txt", "r", True, "utf-8", )
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()
