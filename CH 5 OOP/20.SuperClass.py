class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print("普通员工正在写代码，工资是{}".format(self.salary))


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print("我是一个顾客，爱好{}，地址{}".format(self.favorite, self.address))


# Manager继承了Employee、Customer
class Manager(Employee, Customer):
    def __init__(self, salary, favorite, address):
        print("---Manager的构造方法---")
        # 通过super()函数调用父类的构造方法
        super().__init__(salary)
        # 与上一行功能相同
        # super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类构造方法
        Customer.__init__(self, favorite, address)


m = Manager(25000, "IT", "广州")
m.work()
m.info()
