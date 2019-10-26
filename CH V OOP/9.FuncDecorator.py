# foo函数，该函数将打算作为函数装饰器使用
# 作为函数装饰器使用的函数，它必须定义一个形参
def foo (fn):
	print("foo函数")
	print(fn)
	return "fkjava"

# 被修饰的函数
@foo
def bar():
	print("bar函数")
	
'''
函数装饰器的本质
	（1）将被装饰的函数（bar）作为参数传给装饰器函数（foo）
	（2）被装饰的函数（bar）将被替换成装饰器函数（foo）的返回值
'''
print(bar)# bar被装饰一被替换成装饰器的返回值： fkjava
# 由于bar其实已经被替换成了fkjava，因此bar函数不能被调用
# bar()