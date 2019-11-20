# -*- coding: utf-8 -*-

import threading
import Account


def draw(Account, draw_amount):
    Account.draw(draw_amount)


# 创建一个账户
acct = Account.Account("1234567", 1000)
# 使用两个线程模拟从同一个账户中取钱
threading.Thread(name="甲", target=draw, args=(acct, 800)).start()
threading.Thread(name="乙", target=draw, args=(acct, 800)).start()
