bicyles = ['trek', 'cannondale', 'redline', 'specialized']
# 访问列表元素
print(bicyles)
print(bicyles[0])
print(bicyles[0].title())
print(bicyles[1], bicyles[3])
message = "My first bicyle was a "+bicyles[0].title()+"."
print(message)

# 改变列表元素
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
motorcycle[0] = 'ducati'
print(motorcycle)

# 在列表末尾添加元素
motorcycle.append('honda')
print(motorcycle)
motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')

# insert item
motorcycle.insert(0, 'ducati')


# delete item
# first; need to know the number
del motorcycle[0]
print(motorcycle)

# second; for the last item
# the item which is popped
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

# any location by number
popped_motorcycle = motorcycle.pop(1)
print(popped_motorcycle)

# delete by content,only delet the first
motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.remove('honda')
print(motorcycle)

# sort
cars = ['bmw', 'audi','toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# sort but no change
cars = ['bmw', 'audi','toyota', 'subaru']
sorted_car=sorted(cars)
#just reverse
cars.reverse()
print(cars)

# get length
len(cars)