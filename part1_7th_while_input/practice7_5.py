# 7-5 电影票：
# 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众为10美元；超过12岁的观众为15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价
while True:
    age = input('Please input your age:\n')
    age = int(age)
    if age < 3:
        print('free')
    elif age < 12:
        print('10$')
    else:
        print('15$')
