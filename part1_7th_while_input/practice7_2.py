# 7-2 餐馆订位：
# 编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
number = input('How many you are')
number = int(number)
if number > 8:
    print('There is no table that is enable for 8 people or more people')
else:
    print('There is still table')