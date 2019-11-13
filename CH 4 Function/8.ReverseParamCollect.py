def test(a, b):
    print(a)
    print(b)


vals = {"a": 89, "b": 93}  # 字典

# 用字典的逆向收集，以关键字参数的形式为参数传入参数值
test(**vals)
