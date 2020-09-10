# 7-6 三个出口：
# 以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# ·在while循环中使用条件测试来结束循环。
# ·使用变量active来控制循环结束的时机。
# ·使用break语句在用户输入'quit'时退出循环。

active = True
while active:
    age = input('Please input your age:\n')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print('free')
        elif age < 12:
            print('10$')
        else:
            print('15$')