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
