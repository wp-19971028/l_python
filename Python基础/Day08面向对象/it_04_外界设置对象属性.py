class Cat:
    """
    这是一个猫类
    """


    def eat(self):
        print("%s猫吃鱼" % self.name)

    def drink(self):
        print("%s喝水" % self.name)


# 创建对象

tom = Cat()
tom.name = "Tom"
tom.eat()
# 不可以把name放在后面如果放在后面会报错
#所以不建议把属性放在外面设置
# tom.name = "Tom"
