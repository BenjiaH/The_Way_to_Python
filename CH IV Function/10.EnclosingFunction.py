def foo ():
	print("foo函数")
	def bar ():
		for i in range(5):
			print("bar函数")
	bar()
foo()