def test(a, b):
    print(a)
    print(b)


vals = (20, 40)
# 调用函数时， Python不会对元组自动解包
# 默认情况下，元组是一个整体
# test(vals)

# 对元组进行解包（逆向参数收集）
test(*vals)

msgs = ("aaa", "bbb")
# 调用函数时， Python不会对元组自动解包
# 默认情况下，元组是一个整体
# test(vals)

# 对元组进行解包（逆向参数收集）
test(*msgs)
