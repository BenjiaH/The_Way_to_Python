score = {"语文": 86, "数学": 92, "英语": 91}

# 用一个字典来更新原有的字典：
# 对于已有key，是更新value；对于不存在的key，就是添加key-value
score.update({"语文": 89, "生物": 91})
print(score)

# 使用关键字参数，不支持用表达式
score.update(语文 = 80, 化学 = 93)
print(score)  