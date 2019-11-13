# foo函数，该函数将打算作为函数装饰器使用
# 作为函数装饰器使用的函数，它必须定义一个形参
def foo(fn):
    # print("foo装饰器函数")
    def noname(*args):
        print("---模拟在目标函数之前织入的code---")
        fn(*args)  # fn就是test函数
        print("---模拟在目标函数之后织入的code---")

    return noname


# 被修饰的函数
# 	（1）test函数会被作为参数传给foo()装饰器函数
# 	（2）test函数就被替换成foo装饰器函数的返回值(noname)
@foo
def test(a, b):
    print("test函数")
    print("参数a：", a)
    print("参数b：", b)


'''
函数装饰器的本质
	（1）将被装饰的函数（bar）作为参数传给装饰器函数（foo）
	（2）被装饰的函数（bar）将被替换成装饰器函数（foo）的返回值
'''

test(2, 4)
