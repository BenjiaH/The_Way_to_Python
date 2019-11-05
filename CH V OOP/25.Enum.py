import enum

# 定义Seasons枚举类
Season = enum.Enum("Season", ("SPRING", "SUMMER", "FALL", "WINTER"))
# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season.SPRING.name)
# 访问枚举成员的值
print(Season.SPRING.value)
# 根据枚举变量名访问枚举对象
print(Season["SUMMER"])
# 根据枚举值访问枚举对象
print(Season(3))
