class Tiger():
    # 类方法两点：A、用@classmethod修饰。B、定义一个cls形参
    @classmethod
    def info(cls):
        print("info类方法")
        print(cls)


print(Tiger)
# 类方法属于类本身，因此用类来调用
# 类方法第一个c1s参数也会自动绑定，绑定到调用该方法的类
Tiger.info()

t = Tiger()
t.info()
