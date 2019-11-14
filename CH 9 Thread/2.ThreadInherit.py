# -*- coding: utf-8 -*-

import threading


# 通过继承threading.Thread类来创建线程类
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写run()方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用threading模块的curren_thread()函数获取当前线程
            # 调用线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i += 1


# 主程序（主线程的线程执行体）
for i in range(100):
    # 调用threading模块的current_thread()函数获取当前进程
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        mt1 = MyThread()
        mt1.start()
        # 创建并启动第二个线程
        mt2 = MyThread()
        mt2.start()
print("主线程执行完毕！")
