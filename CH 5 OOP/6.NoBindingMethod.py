class Role:
    def test(self):
        print("test方法")


# test方法本身是实例方法，应该用对象调用
# 但Python允许用类调用实例方法，此时就变成了“未绑定的方法”，因此必须显式为self参数传入参数值
r = Role()
Role.test(r)
