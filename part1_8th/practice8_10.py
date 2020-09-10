# 8-10 了不起的魔术师：
# 在你为完成练习8-9而编写的程序中，编写一个名为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
# 调用函数show_magicians()，确认魔术师列表确实变了。

magicans = ['li','wang','zhang','zhu']
def show_magicans(magicans):
    for magican in  magicans:
        print(magican)
def make_great(magicans):
    for index in range(len(magicans)):
        magicans[index] = 'the great ' + magicans[index]
make_great(magicans)
show_magicans(magicans)