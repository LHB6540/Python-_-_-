# 8-6 城市名：
# 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面这样的字符串：'city,country'至少使用三个城市-国家对调用这个函数，并打印它返回的值。

def city_country(city,country):
    return city + ',' + country

print(city_country('shanghai','China'))
print(city_country('guangzhou','China'))
print(city_country('london','England'))