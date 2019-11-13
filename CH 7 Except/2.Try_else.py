# -*- coding: utf-8 -*-

try:
    a = int(input("请输入第一个整数："))
    b = int(input("请输入第二个整数："))
    print(a / b)
# 同时捕捉两种类型的异常
# 如果你需要访问异常信息，就需要用as为异常指定一个变量名，否则可以省略as子句
except (ValueError, ArithmeticError) as e:
    print(e)
    print(type(e))
# 当程序不出现异常时，就执行else
else:
    print("程序一切正常")
