import enum


class Orientation(enum.Enum):
    # 为序列值指定value值
    EAST = "东"
    SOUTH = "南"
    WEST = "西"
    NORTH = "北"

    def info(self):
        print("这是一个代表方向【{}】的枚举".format(self.value))


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation["WEST"])
# 通过枚举值访问枚举
print(Orientation("南"))
# 调用枚举info方法
Orientation.EAST.info()
# 遍历Orientation枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, "\t->", member, "\t,", member.value)
