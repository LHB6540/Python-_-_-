#9-1 餐馆：
# 创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.restaurant_name=name
        self.cuisine_type=cuisine_type
    def descible_restaurant(self):
        print(self.restaurant_name + " is " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " is opening" )

restaurant = Restaurant("KFC","fast food")
restaurant.descible_restaurant()
restaurant.open_restaurant()
