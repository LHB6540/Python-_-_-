# 7-10 梦想的度假胜地：
# 编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。

place = {}
while True:
    name = input('What is your name：\n')
    place_visit = input('If you could visit one place in the world, where would you go:\n')
    place[name] = place_visit
    next = input('ask for next people:(Yes/No)')
    if next == 'No':
        break

for key,value in place.items():
    print(key+' want to visit '+ value)