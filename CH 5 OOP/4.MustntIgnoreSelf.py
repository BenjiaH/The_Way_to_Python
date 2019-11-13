class Dog:
    def run(self):
        # 一个方法调用其他方法，也需要使用self来调用
        self.jump()
        print("狗在跑")

    def jump(self):
        print("狗在跳")


d = Dog()
d.run()
