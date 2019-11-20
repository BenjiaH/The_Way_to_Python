# -*- coding: utf-8 -*-

import threading
import Account


def draw(Account, draw_amount):
    Account.draw(draw_amount)


# 创建一个账户
acct1 = Account.Account("1", 1000)
acct2 = Account.Account("2", 1000)
# 使用两个线程模拟从同一个账户中取钱
threading.Thread(name="A", target=draw, args=(acct1, 800)).start()
threading.Thread(name="B", target=draw, args=(acct1, 800)).start()
threading.Thread(name="C", target=draw, args=(acct1, 0)).start()
