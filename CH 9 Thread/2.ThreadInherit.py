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
            print(threading.Thread.getName() + " " + str(self.i))
            self.i += 1
