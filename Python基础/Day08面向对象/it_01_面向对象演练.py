class Cat:
    """
    这是一个猫类
    """
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("喝水")

# 创建对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print("%d"%addr)