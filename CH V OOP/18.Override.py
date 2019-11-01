class bird:
    # Bird类的fly()方法
    def fly(self):
        print("飞翔")


class Ostrich(bird):
    # 重写bird类的fly()方法
    def fly(self):
        print("奔跑")


os = Ostrich()
os.fly()
