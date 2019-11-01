class Item:
    def info(self):
        print("Item中的方法：这是一个商品")


class Product:
    def info(self):
        print("Product中的方法：这是一个商品")


class Mouse(Item, Product):
    pass


m = Mouse()
m.info()