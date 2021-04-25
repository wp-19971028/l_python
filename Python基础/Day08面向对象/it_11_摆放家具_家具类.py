class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称
        self.item_list = []

    def __str__(self):
        return ("户型:%s\n总面积:%.2f\n剩余面积%.2f家具名称列表%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("%s添加家具" % item)
        if item.area > self.free_area:
            print("%s面积太大无法添加"%item)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
# print(bed)
# print(chest)
# print(table)
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
