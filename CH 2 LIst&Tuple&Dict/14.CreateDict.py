# key-value
score = {"语文": 85, "数学": 90, "英语": 95}
print(score)

# 要求每个元素只能有2个元素，其中第一个元素是key，第二个元素是va1ue
score1 = dict([("语文", 85), ("数学", 90), ("英语", 95)])
print(score1)

# 用关键字参数来创建dict，此时不允许使用表达式
score2 = dict(语文=85, 数学=90, 英语=95)
print(score2)
