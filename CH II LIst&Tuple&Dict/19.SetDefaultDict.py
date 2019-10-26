score = {"语文": 86, "数学": 92, "英语": 91}

# default用于获取指定key对应的value
print(score.setdefault("语文", 60))

# setdefault如果获取的key不存在时，该方法会为该key设置value
print(score.setdefault("生物", 60))
print(score)