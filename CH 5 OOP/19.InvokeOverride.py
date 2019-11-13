class BaseClass:
    def foo(self):
        print("父类foo")


class SubClass(BaseClass):
    def foo(self):
        print("重写foo")

    def bar(self):
        print("bar方法")
        # 直接调用foo方法，将会调用重写之后的foo方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()
