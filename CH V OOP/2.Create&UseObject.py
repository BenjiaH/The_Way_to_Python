class Person:
	# 构造方法,用于初始化对象的实例变量
	def __init__ (self, name = "Charlie", age = 8):
		self.name = name
		self.age = age

P = Person()
print(P.name, P.age)
P2 = Person("孙悟空")
print(P2.name, P2.age)
P3 = Person(age= 30)
print(P3.name, P3.age)
P4 = Person("白骨精", 23)
print(P4.name, P4.age)
		
class Teacher:
	pass
# Teacher没有定义构造器，因此它只有一个只带se1f参数的构造方法	
# t = Teacher(name = "asdasdas")