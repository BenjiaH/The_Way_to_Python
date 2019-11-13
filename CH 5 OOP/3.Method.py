class User:
    def __init__(self, name="tiger"):
        self.name = name

    def info(self):
        print(self)
        print(self.name)


u = User()
print(u.name)

# User构造的对象，赋值给u2，在User构造器中的self实际上就代表u2
u2 = User("scott")
print(u2.name)
print(u2)

# ---实例方法第一个self不需要传入，由系统自动绑定，总是绑定到方法调用者---
# ---方法中的se1f总是代表该方法的调用者---
u2.info()
