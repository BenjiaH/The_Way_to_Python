class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 装饰器合成了一个只读属性。此时只读属性名与方法名相同
    @property
    def area(self):
        print("getarea")
        return self.width * self.height

    # # 合成了一个计算面积的属性
    # area = property(fget=GetArea, doc="获取面积的属性")

    @property  # 默认是只读属性
    def size(self):
        print("getsize")
        return self.width, self.height

    @size.setter  # 装饰出setter方法
    def size(self, size):
        print("setsize")
        self.width = size[0]
        self.height = size[1]


r = Rectangle(30, 40)
# 访问area实例变量（实际上就是调用getter方法）
print(r.area)

# 访问size属性（实际上就是调用getter方法）
print(r.size)
# 对size属性赋值（实际上就是调用中setter方法）
r.size = (5, 6)

print(r.area)
