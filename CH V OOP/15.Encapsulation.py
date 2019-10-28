class User:
    def __hide(self):
        print("示范隐藏的hide方法")

    def gatname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError("用户名长度必须在3-8位之间！")
