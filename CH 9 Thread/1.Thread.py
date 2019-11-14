# -*- coding: utf-8 -*-

import threading


# 定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
    for i in range(max):
        # 调用threading模块的current_thread()函数获取当前线程
        # 调用线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))


# 主程序
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() + " " + str(i))
    if i == 2:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        # 创建并启动第二个线程
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print("主线程执行完成！")
