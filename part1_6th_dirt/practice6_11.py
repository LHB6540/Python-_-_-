# 6-11 城市：
# 创建一个名为cities的字典，其中将三个城市名用作键；
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country、population和fact等键。
# 将每座城市的名字以及有关它们的信息都打印出来。

cities = {
    'guangzhou': {
        'country': 'China',
        'population': '100m',
        'fact':'breakfast is perfect'
    },
    'London': {
        'country': 'England',
        'popultion': '20m',
        'fact':'always raining'
    },
    'NewYork': {
        'country': 'USA',
        'popultion': '50m',
        'fact': 'boom'
    }
}
for key, value in cities.items():
    print('Here is the info of ' + key + ':')
    for city_key, city_value in value.items():
        print(city_key + ':'+ city_value)
    print('\n')