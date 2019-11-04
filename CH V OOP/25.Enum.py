import enum

# 定义Seasons枚举类
Season = enum.Enum(Season, ("SPRING", "SUMMER", "FALL", "WINTER"))
print(Season(3))
