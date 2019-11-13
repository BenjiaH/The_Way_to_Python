class Tiger():
    # 静态方法两点：A、用@staticmethod修饰。B、定义一个cls形参
    @staticmethod
    def info(p):
        print("info静态方法")
        print(p)


# 静态方法相当于一个函数，因此不会自动绑定
# 类调用静态方法，因此必须为参数传入参数值
Tiger.info("hhhh")

t = Tiger()
# 对象调用静态方法，也不会自动绑定，因此必须为参数传入参数值
t.info(t)

'''
				是否自动绑定参数
			实例方法		类方法		静态方法
对象调用		是			是			否
类调用		否			是			否
'''
