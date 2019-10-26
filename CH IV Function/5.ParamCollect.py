def test (num, *books):
	print("num:", num)
	print("books:", books)

# 将多个值自动封装成元组	
test(5, "fkjava", "crazyit", "wawa")

def info (*names, msg):
	for name in names:
		print("%s %s" % (name, msg))
		
info("AAA", "BBB", "CCC", msg = "DDD")