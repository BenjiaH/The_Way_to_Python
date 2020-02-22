# -*-coding:utf-8-*-

# f = open("D:\\OneDrive\\Python_project\\CSDN_Python\\CH 6 File\\abc.txt", "r", True, "utf-8")
f = open(r"D:\OneDrive\Python_project\CSDN_Python\CH 6 File\abc.txt", "r", True, "utf-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()
