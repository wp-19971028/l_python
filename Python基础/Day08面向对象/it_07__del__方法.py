class Cat:
    def __init__(self, name):
        print("这是一个初始化方法!")
        self.name = "Tom"

    def __del__(self):
        print("%s 销毁了" % self.name)

    def eat(self):
        print("%s猫吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)


tom = Cat("Tom")
tom.drink()
# del 可以用来销毁对象
del tom
print("_"*50)
