# 定义ItemMetaClass，继承type
class ItemMetaClass(type):
    # cls代表被动态修改的类
    # name代表被动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 为该类动态添加一个cal_price方法
        attrs["cal_price"] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)


# 定义book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ("name", "price", "_discount")

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义cellphone类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ("price", "_discount")

    def __init__(self):
