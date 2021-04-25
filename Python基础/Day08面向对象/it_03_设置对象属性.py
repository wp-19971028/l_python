class Cat:
    """
    这是一个猫类
    """
    name = ""

    def eat(self):
        print("%s猫吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)


# 创建对象

tom = Cat()

tom.name = "Tom"
tom.eat()
