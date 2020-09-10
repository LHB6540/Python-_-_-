# 8-8 用户的专辑：
# 在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。
# 在这个while循环中，务必要提供退出途径。

def make_album(singer,album):
    return {'singer':singer,'album':album}
while True:
    print('you can quit by input "q" at any time')
    singer = input('input signer\'s name')
    if singer == 'q':
        break
    album = input('input album\'s name')
    if 'album' == 'q':
        break
    print(make_album(singer,album))

