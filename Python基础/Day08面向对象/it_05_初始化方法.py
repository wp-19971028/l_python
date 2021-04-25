class Cat:
    def __init__(self):
        print("这是一个初始化方法!")
        self.name = "Tom"
    def eat(self):
        print("%s猫吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)

tom = Cat()
print(tom.name)