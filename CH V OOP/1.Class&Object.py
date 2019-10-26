class User:
	print("User类")


class Item:
	print("Item类")
	itemtype = "电子产品"
	itemcolor = "未知"

print("种类：", Item.itemtype)
print("颜色：", Item.itemcolor)
Item.foo = "测试"
print(Item.foo)

class Book:
	print("Book")
	booktype = "IT图书"
		
	# 定义方法与定义函数几乎一样
	# 实例方法，第一个参数推荐使用self（并不强制），这样有更好的可读性	
	def desc (self):
		self.name = "疯狂Python讲义"
		self.price = 118
		price("图书是%s,价格是%d" % (self.name, self.price))
		
	def haha (self):
		print("一个haha方法")