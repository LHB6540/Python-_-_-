# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
# 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.restaurant_name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def descible_restaurant(self):
        print(self.restaurant_name + " is " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is opening" )
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,numbers):
        self.number_served+=numbers
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavors=['blue','red','yellow']
    def showIce(self):
        print("Here is the Ice:")
        for i in self.flavors:
            print(i)
ice=IceCreamStand('Hi','IceCream')
ice.showIce()