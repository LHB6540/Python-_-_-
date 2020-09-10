# 8-14 汽车：
# 编写一个函数，将一辆汽车的信息存储在一个字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。
# 这个函数必须能够像下面这样进行调用：car = make_car(...)
# 打印返回的字典，确认正确地处理了所有的信息。

def make_car(type,No,**info):
    car_info = {}
    car_info['type'] = type
    car_info['No'] = No
    for key,value in info.items():
        car_info[key] = value
    return car_info
car =make_car('audi','A5',color='blue',fastest='180KN',use_time='2s')
print(car)