# 9-9 电瓶升级：
# 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
# 这个方法检查电瓶容量，如果它不是85，就将它设置为85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range()。你会看到这辆汽车的续航里程增加了。

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+ self.make+" "+ self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+ " miles on it")
    def update_odometer(self,mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")
        self.odometer_reading=mileage
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message= "This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

electricecar=ElectricCar("tosla","Model S","2016")
electricecar.battery.get_range()
electricecar.battery.upgrade_battery()
electricecar.battery.get_range()
