class Plant:
    def __init__(self, height=2):
        self.height = height

    def grow(self):
        self.height += 10
        return self


p = Plant()
print(p.height)
# 如果grow方法 return self-self本身又代表方法调用者：p
p.grow().grow().grow().grow()  # grow四次
print(p.height)
