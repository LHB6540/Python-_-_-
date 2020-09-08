# 5-5 外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。
# ·如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
# ·如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
# ·如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
# ·编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息
alien_color = 'green'
if alien_color == 'green':
    print('You get 5 point')
elif alien_color=='yellow':
    print('You get 10 point')
else:
    print('You get 15 point')

alien_color = 'yellow'
if alien_color == 'green':
    print('You get 5 point')
elif alien_color=='yellow':
    print('You get 10 point')
else:
    print('You get 15 point')

alien_color = 'red'
if alien_color == 'green':
    print('You get 5 point')
elif alien_color=='yellow':
    print('You get 10 point')
else:
    print('You get 15 point')