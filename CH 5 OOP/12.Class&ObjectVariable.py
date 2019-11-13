class User:
    # 类空间中定义的变量，是类变量
    category = "未知类型"

    def __init__(self, name="admin", passwd="passwd"):
        # 通过se1f引用赋值的变量，是实例变量
        self.name = name
        self.passwd = passwd


# 通过类引用赋值的变量，类变量
User.type = "通用用户"
print(User.category)

User.category = "改变后的类型"
print(User.category)

us = User()
# 当对象本身没有 category实例变量时，对象可访问该类变量
print(us.category)

# 只要通过对象对变量赋值，就变成了新增实例变量
us.category = "实例类型"

# 当对象本身有 category实例变量时，对象优先访问该实例变量
print(us.category)
print(User.category)
