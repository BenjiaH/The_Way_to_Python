# -*- coding: utf-8 -*-

import threading
import time


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    def get_balance(self):
        return self.balance

    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票：" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t" + threading.current_thread().name + "余额为：" + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()
