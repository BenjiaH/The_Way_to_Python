# -*- coding: utf-8 -*-

f = None
try:
    f = open("abc.txt", "r", True)
    print(f.read())
except:
    print("捕捉到异常")
finally:
    # 程序要判断，f不为None才需要c1ose
    if f:
        # 在finally块中嵌套了异常处理
        try:
            f.close()
        except:
            print("捕捉到关闭异常")
