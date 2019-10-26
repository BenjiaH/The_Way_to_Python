def foo ():
	print("foo函数")
	def bar ():
		for i in range(5):
			print("bar函数")
	# bar()
	# bar表示函数本身（函数也相当于一个值，是 function类型的值）
	# bar()表达调用（执行）函数
	return bar
	
r = foo()
r()
print()
print()
foo()()