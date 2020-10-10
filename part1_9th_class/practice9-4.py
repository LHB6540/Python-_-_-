# 9-4 就餐人数：
# 在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

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

restaurant=Restaurant("KFC","Fast food")
print(restaurant.number_served)
restaurant.number_served=10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(30)
print(restaurant.number_served)