mylist = [20, "fkjava", 3.4]
# 自动解包，列表中的3个值自动赋值给3个变量
a, b, c = mylist
print(a)
print(b)
print(c)

mytuple = ("python", "kotlin", "swift", "java", "go", "spring", "swx")
first, *rest = mytuple
print(first)
print(rest)
