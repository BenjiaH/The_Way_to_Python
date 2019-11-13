score = {"语文": 85, "数学": 90, "英语": 95}

# 对不存在key赋值，就是添加key-va1ue对
score["生物"] = 91
print(score)

# 删除key-value对
del score["数学"]
print(score)
