#访问
alien={'color':'green','point':5}
print(alien['color'])

#添加
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

#空字典
#alien = {}

#修改字典值
alien['x_position'] = 25
print(alien['x_position'])

alien['speed'] = 'medium'
x_increment = 1
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print(alien)

#删除
del alien['point']
print(alien)

#格式
alien = {
     'point': 5, 'x_position': 27,
    'color': 'green',
     'y_position': 25,
    }
print(alien)

#遍历键-值
for key, value in alien.items():
    print('\nKey:' + key + ' Value:' + str(value))
#遍历键
for key in alien.keys():
    print(key)
#按顺序
for key in sorted(alien.keys()):
    print(key)
print(alien.values())
#遍历值
for value in alien.values():
    print(value)

# 字典列表
alien_0 = {
     'point': 5, 'x_position': 27,
    'color': 'green',
     'y_position': 25,
    }
alien_1 = {
     'point': 15, 'x_position': 22,
    'color': 'green',
     'y_position': 25,
    }
alien_2 = {
     'point': 5, 'x_position': 26,
    'color': 'green',
     'y_position': 25,
    }
alien_list = [alien_0, alien_1, alien_2]
print(alien_list)

aliens = []
for i in range(30):
    new_alien={'point': 5, 'x_position': 26,
    'color': 'green',
    'y_position': 25,
    }
    aliens.append(new_alien)
for alien_ in aliens[0:5]:
    print(alien_)


# 列表字典
pizza = {'crust': 'thick', 'mushrooms': ['mushrooms', 'extra cheese']}
print('You order a ' + pizza['crust'] + ' pizza with the following topping:')
for topping in pizza['mushrooms']:
    print(topping)

# 字典字典
aliens_dic = {
    'a': {'point': 5, 'x_position': 26, 'color': 'green', 'y_position': 25},
    'b':{'point': 5, 'x_position': 26, 'color': 'green', 'y_position': 25},
}
