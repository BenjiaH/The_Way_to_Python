class Dog:
    __slots__ = ("walk", "age", "name")

    def __init__(self, name):
        self.name = name

    def test(self):
        print("预先定义的test方法")


d = Dog("Snoopy")
from types import MethodType

# 只允许为实例动态添加walk、age、name这三个属性或方法
d.walk = MethodType(lambda self: print("{}正在慢慢走".format(self.name)), d)
d.age = 5
d.walk()
# d.foo() = 30

Dog.bar = lambda self: print("abc")
d.bar()


class GunDog(Dog):
    def __init__(self, name):
        super(GunDog, self).__init__(name)
        pass


gd = GunDog("Puppy")
gd.speed = 90
print(gd.speed)
